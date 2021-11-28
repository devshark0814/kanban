<template>
    <v-container>
        <v-row>
            <v-col>
                <v-card>
                    <v-card-title primary-title>
                        Login
                    </v-card-title>
                    <v-card-text>
                        <v-text-field
                            label="User Name"
                        ></v-text-field>
                        <v-text-field
                            name="password"
                            label="Enter your password"
                            type="password"
                        ></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" dark>ログイン</v-btn>
                        <v-btn color="primary" dark @click="$refs.new_account.onOpen()">新規作成</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        <NewAccount ref="new_account"/>
    </v-container>
</template>
<script src="./Login.js"></script>
<style src="./Login.css"></style>