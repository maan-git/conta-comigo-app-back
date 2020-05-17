/* eslint-disable no-shadow */

const APPEND_NOTIFICATION = 'APPEND_NOTIFICATION';
const DELETE_NOTIFICATION = 'DELETE_NOTIFICATION';
const UPDATE_STATUS = 'UPDATE_STATUS';
const SET_VISIBLE_NOTIFICATION = 'SET_VISIBLE_NOTIFICATION';
const MAX_NOTIFICATIONS_TO_SHOW = 3;

const NOTIFICATION_STATUS = {
  UNREAD: 0,
  READ: 1,
};

const state = {
  allNotifications: [],
  notificationsToShow: [],
  visibleNotification: null,
};

let visibleNotificationTimeout = null;

const clearCurrentTimeout = () => {
  if (visibleNotificationTimeout) {
    clearTimeout(visibleNotificationTimeout);
    visibleNotificationTimeout = null;
  }
};

const REQUIRED_PROPERTIES = [
  'id',
  'description',
  'type',
  'status',
];

const checkRequiredProperties = (notification) => {
  REQUIRED_PROPERTIES.forEach((prop) => {
    if (!(prop in notification)) {
      throw new Error(`Property ${prop} is mandatory in notification`);
    }
  });
};

const checkIsNotificationObject = (notification) => {
  if (!notification || typeof notification !== 'object') {
    throw new Error('Notification should be an object instance');
  }

  checkRequiredProperties(notification);
};

const getters = {
  getVisibleNotification(state) { return state.visibleNotification; },

  getUnreadedNotifications(state) {
    const filter = (notification) => notification.status_id === NOTIFICATION_STATUS.UNREAD;
    return state.allNotifications.find(filter) ?? [];
  },

  hasUnreadNotifications(state, getters) {
    return getters.getUnreadedNotifications > 0;
  },
};

const actions = {
  showNotification({ commit, state, dispatch }, notification) {
    checkIsNotificationObject(notification);

    if (state.visibleNotification !== null) {
      commit(APPEND_NOTIFICATION, notification);
    } else {
      dispatch('setVisibleNotification', notification);
    }
  },

  removeNotification({ commit, state, dispatch }) {
    clearCurrentTimeout();
    commit(SET_VISIBLE_NOTIFICATION, null);
    if (state.notificationsToShow.length) {
      dispatch('setVisibleNotification', state.notificationsToShow[0]);
    }
  },

  setVisibleNotification({ commit, dispatch }, notification) {
    clearCurrentTimeout();

    commit(DELETE_NOTIFICATION, notification);
    commit(SET_VISIBLE_NOTIFICATION, notification);

    visibleNotificationTimeout = setTimeout(() => {
      dispatch('removeNotification');
    }, 6000);
  },
};

const mutations = {
  [APPEND_NOTIFICATION](state, notification) {
    if (state.notificationsToShow.length === MAX_NOTIFICATIONS_TO_SHOW) {
      state.notificationsToShow.splice(0, 1);
    }

    state.notificationsToShow.push(notification);
  },

  [DELETE_NOTIFICATION](state, notification) {
    const filter = (n) => notification.id === n.id;
    const notificationIndex = state.notificationsToShow.findIndex(filter);

    if (notificationIndex >= 0) {
      state.notificationsToShow.splice(notificationIndex, 1);
    }
  },

  [UPDATE_STATUS](state, notificationId, newStatus) {
    const filter = (notification) => notification.id === notificationId;
    const notification = state.allNotifications.find(filter);

    if (notification) {
      notification.status = newStatus;
    }
  },
  [SET_VISIBLE_NOTIFICATION](state, notification) {
    state.visibleNotification = notification;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
