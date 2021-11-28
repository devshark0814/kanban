import apiClient from "../../common/apiClient.js";
import { $CommonJs } from "../../common/common.js";
export default {
    data() {
        return{
            displayFlag: false,
            userModel: {
                first_name    : "",
                last_name     : "",
                email         : "",
                password      : "",
                img_url       : ""
            }
        }
    },

    watch: {
        displayFlag: function(newVal, oldVal) {
            if(newVal) {
                this.userModel = {};
            }
        }
    },

    methods: {
        onOpen() {
            this.displayFlag = true;
        },
        onCreate: async function() {
            const response = await this.$apiClient.post("/api/user/user", this.userModel);
            this.$toasted.success(response.data.message, $CommonJs.getSuccessToastOptions());
            this.displayFlag = false;
        }
    }
};
