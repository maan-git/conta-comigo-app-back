import store from '../store';

const notificationActions = {
  showNotification: (notification) => {
    store.dispatch('notification/showNotification', notification);
  },
};

const HEARTBEAT = '--heartbeat--';

class WS4Redis {
  constructor(options) {
    this.opts = { ...{ heartbeat_msg: null }, ...options };

    if (options.uri === undefined) {
      throw new Error('No Websocket URI in options');
    }

    this.ws = null;
    this.timer = null;
    this.attempts = 1;
    this.mustReconnect = true;
    this.heartbeatInterval = null;
    this.missedHeartbeats = 0;

    this.connect(this.opts.uri);
  }

  // this code is borrowed from http://blog.johnryding.com/post/78544969349/
  //
  // Generate an interval that is randomly between 0 and 2^k - 1, where k is
  // the number of connection attmpts, with a maximum interval of 30 seconds,
  // so it starts at 0 - 1 seconds and maxes out at 0 - 30 seconds
  generateInteval = (k) => {
    let maxInterval = (2 ** k - 1) * 1000;

    // If the generated interval is more than 30 seconds, truncate it down to 30 seconds.
    if (maxInterval > 30 * 1000) {
      maxInterval = 30 * 1000;
    }

    // generate the interval to a random number between 0 and the
    // maxInterval determined from above
    return Math.random() * maxInterval;
  }

  isClosing = () => this.ws && this.ws.readyState === 2;

  isClosed = () => this.ws && this.ws.readyState === 3;

  sendHeartbeat = () => {
    try {
      this.missedHeartbeats += 1;
      if (this.missedHeartbeats > 3) {
        throw new Error('Too many missed heartbeats.');
      }
      this.ws.send(this.opts.heartbeat_msg);
    } catch (e) {
      clearInterval(this.heartbeatInterval);
      this.heartbeatInterval = null;
      // console.warn(`Closing websocket connection. Reason: ${e.message}`);
      if (!this.isClosing() && !this.isClosed()) {
        this.ws.close();
      }
    }
  }

  onOpen = () => {
    // new connection, reset attemps counter
    this.attempts = 1;
    if (this.opts.heartbeat_msg && this.heartbeatInterval === null) {
      this.missedHeartbeats = 0;
      this.heartbeatInterval = setInterval(this.sendHeartbeat, 5000);
    }
    if (typeof this.opts.connected === 'function') {
      this.opts.connected();
    }
  }

  onError = () => {
    // console.error('Websocket connection is broken!');
  }

  onMessage = (evt) => {
    if (this.opts.heartbeat_msg && evt.data === this.opts.heartbeat_msg) {
      // reset the counter for missed heartbeats
      this.missedHeartbeats = 0;
    }

    if (typeof this.opts.receive_message === 'function') {
      this.opts.receive_message(evt.data);
    }
  }

  sendMessage = (message) => {
    this.ws.send(message);
  };

  getState = () => this.ws.readyState;

  isConnecting = () => this.ws && this.ws.readyState === 0;

  isConnected = () => this.ws && this.ws.readyState === 1;

  close = () => {
    clearInterval(this.heartbeatInterval);
    this.mustReconnect = false;
    if (!this.isClosing() || !this.isClosed()) {
      this.ws.close();
    }
  };

  tryToReconnect = () => {
    if (this.mustReconnect && !this.timer) {
      // console.log('Reconnecting...');
      const interval = this.generateInteval(this.attempts);
      this.timer = setTimeout(() => {
        this.attempts += 1;
        this.connect(this.ws.url);
      }, interval);
    }
  }

  onClose = (evt) => {
    // console.log('Connection closed!');
    if (typeof this.opts.disconnected === 'function') {
      this.opts.disconnected(evt);
    }
    this.tryToReconnect();
  }

  connect = (uri) => {
    try {
      if (this.ws && (this.isConnecting() || this.isConnected())) {
        // console.log('Websocket is connecting or already connected.');
        return;
      }

      if (typeof this.opts.connecting === 'function') {
        this.opts.connecting();
      }

      // console.log(`Connecting to ${uri} ...`);
      this.ws = new WebSocket(uri);
      this.ws.onopen = this.onOpen;
      this.ws.onmessage = this.onMessage;
      this.ws.onerror = this.onError;
      this.ws.onclose = this.onClose;
      this.timer = null;
    } catch (err) {
      this.tryToReconnect();
    }
  }
}

function onConnecting() {
  // console.log('Websocket is connecting...');
}

function onConnected() {
  // console.log('Connected');
}

function onDisconnected() {
  // console.log(`Websocket was disconnected: ${JSON.stringify(evt)}`);
}

// receive a message though the websocket from the server
function receiveMessage(msg) {
  if (msg !== HEARTBEAT) {
    const msgObj = JSON.parse(msg);
    const n = {
      id: msgObj.id,
      description: msgObj.content,
      type: msgObj.type_id,
      status: 0,
    };

    notificationActions.showNotification(n);
  }
  // console.log(`Message from Websocket: ${msg}`);
}

let client = null;

const connect = () => {
  client = new WS4Redis({
    uri: 'ws://conta-comigo-ap.herokuapp.com/ws/frontend?subscribe-user',
    connecting: onConnecting,
    connected: onConnected,
    receive_message: receiveMessage,
    disconnected: onDisconnected,
    heartbeat_msg: HEARTBEAT,
  });
};

const disconnect = () => {
  client.close();
};

export default {
  startListening() {
    connect();
  },
  stopListening() {
    disconnect();
  },
};
