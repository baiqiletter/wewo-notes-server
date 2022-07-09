<!-- <template>
  <el-menu
    class="main-menu"
    background-color="#2A2D33"
    text-color="#fff"
    :collapse="isCollapse"
    unique-opened
    router
  >
    <el-menu-item class="menu-item" index="/monitor">
      <el-icon><img src="@/assets/icons/icon_m_home.svg" /></el-icon>
      <span>驾驶舱</span>
    </el-menu-item>
    <el-sub-menu class="menu-item" index="/alerts">
      <template #title>
        <el-icon><img src="@/assets/icons/icon_m_sjgj.svg" /></el-icon>
        <span>事件告警</span>
      </template>
      <el-menu-item index="/alerts/unresolved">
        <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
        <span>未解决告警</span>
      </el-menu-item>
      <el-menu-item index="/alerts/resolved">
        <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
        <span>已解决告警</span>
      </el-menu-item>
    </el-sub-menu>
    <el-sub-menu class="menu-item" index="/statistics">
      <template #title>
        <el-icon><img src="@/assets/icons/icon_m_tjfx.svg" /></el-icon>
        <span>统计分析</span>
      </template>
      <el-menu-item index="/statistics/risk">
        <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
        <span>风险事件统计</span>
      </el-menu-item>
      <el-menu-item index="/statistics/alert">
        <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
        <span>设备告警统计</span>
      </el-menu-item>
    </el-sub-menu>
    <el-sub-menu class="menu-item" index="/devices">
      <template #title>
        <el-icon><img src="@/assets/icons/icon_m_xtsz.svg" /></el-icon>
        <span>系统管理</span>
      </template>
      <el-menu-item index="/users">
        <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
        <span>用户管理</span>
      </el-menu-item>
      <el-menu-item index="/depts">
        <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
        <span>部门管理</span>
      </el-menu-item>
      <el-sub-menu index="">
        <template #title>
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>设备管理</span>
        </template>
        <el-menu-item index="/devices/ai">
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>AI设备管理</span>
        </el-menu-item>
        <el-menu-item index="devices/nvr">
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>NVR管理</span>
        </el-menu-item>
        <el-menu-item index="/devices/camera">
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>摄像头管理</span>
        </el-menu-item>
        <el-menu-item index="/devices/alg">
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>算法管理</span>
        </el-menu-item>
        <el-menu-item index="/devices/manufacturers">
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>设备厂商</span>
        </el-menu-item>
        <el-menu-item index="/devices/areas">
          <el-icon><img src="@/assets/icons/icon_m2.svg" /></el-icon>
          <span>区域管理</span>
        </el-menu-item>
      </el-sub-menu>
    </el-sub-menu>

    <el-menu-item index="">
      <div style="width: 100%" @click="collapse">
        <el-icon><img src="@/assets/icons/icon_navba_expand.svg" /></el-icon>
      </div>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref, defineExpose } from "vue";
const isCollapse = ref(false);

const collapse = () => {
  if (isCollapse.value === true) {
    isCollapse.value = false;
  } else {
    isCollapse.value = true;
  }
};

defineExpose({
  isCollapse
})
</script>

<script lang="ts">
export default {
  name: "NavBar",
};
</script>

<style>
.main-menu span {
  font-size: 16px;
}
</style> -->