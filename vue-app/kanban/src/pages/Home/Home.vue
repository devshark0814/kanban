<template>
    <div>
        <h1>Home画面</h1>
        <div></div>
        <input type="button" value="button" @click="getIp">
    </div>
</template>
<script>
    export default {
        name: "SearchIp",
        methods: {
            getIp() {
                this.axios
                    .get("http://localhost:3000/api/hello")
                    .then((response) => {
                        alert(response.data.origin);
                    })
                    .catch((e) => {
                        alert(e);
                    });
            },
        },
    };
</script>