<template>
  <div>
    <div>
      <b-navbar
        toggleable="lg"
        type="dark"
        variant="primary"
        class="navbar-horizontal"
      >
        <b-navbar-brand href="#">PRIMARY COLOR</b-navbar-brand>
      </b-navbar>
    </div>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// import { defineComponent } from "vue";

// export default defineComponent({
//   components: {},
//   setup() {},
// });
</script>

<style scoped>
.layout-container-demo .el-header {
  position: relative;
  background-color: var(--el-color-primary-light-7);
  color: var(--el-text-color-primary);
}
.layout-container-demo .el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}
.layout-container-demo .el-menu {
  border-right: none;
}
.layout-container-demo .el-main {
  padding: 0;
}
.layout-container-demo .toolbar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  right: 20px;
}
</style>
