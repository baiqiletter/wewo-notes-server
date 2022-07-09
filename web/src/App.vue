<script setup>
import { RouterView } from "vue-router";
// import NavBar from "@/components/NavBar.vue";

import { reactive } from "vue";
const isCollapseRef = reactive({ isCollapse: false });
</script>

<template>
  <RouterView />
</template>


<style>
.el-main {
  padding: 0px;
}
</style>