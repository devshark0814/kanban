// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import axios from "axios"; //追記
import VueAxios from "vue-axios"; //追記
import vuetify from "@/plugins/vuetify"; // path to vuetify export
import Toasted from 'vue-toasted';

Vue.config.productionTip = false;

Vue.use(VueAxios, axios); //追記
Vue.use(Toasted);

import apiClient from "./common/apiClient";
//共通レスポンス処理
apiClient.interceptors.response.use(
    function (response) {
        // 成功時の処理
        return response;
    },
    function (error) {
        // 失敗時の処理
        switch (error.response.status) {
            case 401:
            // HTTPステータスに応じて処理
            case 403:
            default:
            // 例外処理
        }
    }
);

/* eslint-disable no-new */
new Vue({
    el: "#app",
    router,
    components: { App },
    template: "<App/>",
    vuetify
});
