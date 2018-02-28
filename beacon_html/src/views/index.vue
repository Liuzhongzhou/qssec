<style>

</style>
<template>
    <div>
        <framework>
            <router-view slot="content"></router-view>
        </framework>
    </div>
</template>
<script>
    import framework from './framework.vue'
    export default {
        data() {
            return {

            }
        },
        computed:{

        },
        mounted() {

        },
        methods: {

        },
        components: {
            framework
        }
    };
</script>