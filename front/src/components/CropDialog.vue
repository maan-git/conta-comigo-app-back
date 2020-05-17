<template>
  <div>
    <v-dialog v-model="dialog" max-width="520">
      <v-card max-width="520" raised>
        <v-card-title class="headline primary--text">
          <span>Adicione uma foto para o seu perfil</span>
          <v-spacer></v-spacer>
          <v-btn
            icon
            @click="dialog=false"
          ><v-icon>mdi-close</v-icon></v-btn>
        </v-card-title>
        <v-card-text>
          <v-file-input
            :prepend-icon="null"
            v-model="selectedFile"
            accept="image/png, image/jpeg"
            label="Foto"
            placeholder="Selecione a imagem"
            outlined
            :show-size="1024"
            class="my-4"
            @change="setupCropper"
          ></v-file-input>
          <v-row v-if="objectUrl">
            <v-col cols="12" sm="6" class="text-center">
              <div class="overline">Original</div>
              <div class="image-container elevation-4">
                <img class="image-preview" ref="source" :src="objectUrl">
              </div>
              <div class="d-flex justify-center">
                <v-btn icon small @click="resetCropper">
                  <v-icon small>mdi-aspect-ratio</v-icon>
                </v-btn>
                <div class="mx-2">
                  <v-btn icon small @click="rotateLeft">
                    <v-icon small>mdi-rotate-left</v-icon>
                  </v-btn>
                  <v-btn icon small @click="rotateRight">
                    <v-icon small>mdi-rotate-right</v-icon>
                  </v-btn>
                </div>
              </div>
            </v-col>
            <v-col cols="12" sm="6" class="text-center">
              <div class="overline">Preview</div>
              <div class="image-container elevation-4">
                <img class="image-preview" :src="previewCropped">
              </div>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            rounded
            large
            color="primary"
            :disabled="!objectUrl"
            @click="saveCrop"
          >
            <span>Salvar</span>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import Cropper from 'cropperjs';
import debounce from 'lodash/debounce';
import { mapState } from 'vuex';

export default {
  computed: mapState(['register']),
  data() {
    return {
      dialog: false,
      cropper: null,
      objectUrl: null,
      previewCropped: null,
      selectedFile: null,
      debouncedUpdatePreview: debounce(this.updatePreview, 257),
    };
  },
  methods: {
    setupCropper(selectedFile) {
      if (this.cropper) {
        this.cropper.destroy();
      }

      if (this.objectUrl) {
        window.URL.revokeObjectURL(this.objectUrl);
      }

      if (!selectedFile) {
        this.cropper = null;
        this.objectUrl = null;
        this.previewCropped = null;
        return;
      }

      this.objectUrl = window.URL.createObjectURL(selectedFile);
      this.$nextTick(this.setupCropperInstance);
    },
    setupCropperInstance() {
      this.cropper = new Cropper(this.$refs.source, {
        aspectRatio: 1,
        crop: this.debouncedUpdatePreview,
      });
    },
    updatePreview() {
      const canvas = this.cropper.getCroppedCanvas();
      this.previewCropped = canvas.toDataURL('image/png');
    },
    resetCropper() {
      this.cropper.reset();
    },
    rotateLeft() {
      this.cropper.rotate(-90);
    },
    rotateRight() {
      this.cropper.rotate(90);
    },
    saveCrop() {
      this.$emit('avatar', this.previewCropped);
      this.$store.dispatch('register/setAvatar', this.previewCropped);
      this.dialog = false;
    },
    open() {
      this.dialog = true;
    },
  },
};
</script>
<style lang="scss" scoped>
.image-container {
  display: inline-block;
}

.image-preview {
  display: block;
  max-height: 229px;
  max-width: 100%;
}
</style>
<style lang="scss">
  @import './../../node_modules/cropperjs/dist/cropper.css';
</style>
