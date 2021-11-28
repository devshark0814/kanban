<template>
    <v-container v-if="displayFlag">
        <v-row>
            <v-col>
                <v-card>
                    <v-card-title primary-title>
                        New Accouont
                    </v-card-title>
                    <v-card-text>
                        <v-text-field
                            label="User Name"
                            v-model="userModel.first_name"
                        ></v-text-field>
                        <v-text-field
                            label="User Name"
                            v-model="userModel.last_name"
                        ></v-text-field>
                        <v-text-field
                            name="email"
                            label="email"
                            v-model="userModel.email"
                        ></v-text-field>
                        <v-text-field
                            name="password"
                            label="Enter your password"
                            v-model="userModel.password"
                        ></v-text-field>
                        <v-text-field
                            name="img_url"
                            label="アイコン画像"
                            v-model="userModel.img_url"
                        ></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" dark @click="displayFlag=false">キャンセル</v-btn>
                        <v-btn color="primary" dark @click="onCreate">登録</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./NewAccount.js"></script>
<style src="./NewAccount.css"></style>