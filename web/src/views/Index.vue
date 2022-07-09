<template>
  <div class="login-main">
    <div class="login-form">
      <div style="display: flex; flex-direction: column; margin-right: 200px">

        <h2>FLOMO WEWO</h2>
      </div>
      <el-form
        ref="loginFormRef"
        :rules="rules"
        label-width="80px"
        :model="loginForm"
      >
        <el-form-item label="用户名" prop="username">
          <el-input
            v-model="loginForm.username"
            placeholder="请输入用户名"
            @keyup.enter="login(loginFormRef)"
          />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="loginForm.password"
            type="password"
            placeholder="请输入密码"
            @keyup.enter="login(loginFormRef)"
            show-password
          />
        </el-form-item>
        <div style="text-align: center">
          <el-button type="primary" @click="login(loginFormRef)">
            登录
          </el-button>
          <el-button type="danger" @click="register()">注册</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref, getCurrentInstance} from "vue";
import type { FormInstance } from "element-plus";
import { useRouter } from "vue-router";

let { proxy } = getCurrentInstance();

const router = useRouter();

const loginFormRef = ref<FormInstance>();

const checkUsername = (rule: any, value: any, callback: any) => {
  if (!value) {
    return callback(new Error("请输入用户名"));
  } else {
    // 满足规则执行回调函数
    callback();
  }
};

const checkPassword = (rule: any, value: any, callback: any) => {
  if (!value) {
    return callback(new Error("请输入密码"));
  } else {
    // 满足规则执行回调函数
    callback();
  }
};

const loginForm = reactive({
  username: "",
  password: "",
});

const rules = reactive({
  username: [{ validator: checkUsername, trigger: "blur" }],
  password: [{ validator: checkPassword, trigger: "blur" }],
});

const login = (loginFormRef) => {
  loginFormRef.validate(async (valid) => {
    if (valid) {
      
      await proxy.axios.post("http://"+ document.domain +":8000/login", {
          username: loginForm.username,
          password: loginForm.password,
        })
        .then((response) => {
          if (response.data.code == 1) {
            proxy.$message.success("登录成功！");
            window.sessionStorage.setItem("username", response.data.username);
            router.push("/");
          } else {
            proxy.$message.error("登录失败！");
          }
        });
    }
  });
};

const register = () => {
  router.push("/register");
};
</script>


<!-- <script lang="ts">
export default {
  name: "AdminIndex",
  methods: {
    login() {
      this.loginFormRef.validate(async (valid) => {
        if (valid) {
          await this.axios
            .post("http://wuud.fun:8000/login", {
            // .post("/login", {
              username: this.loginForm.username,
              password: this.loginForm.password,
            })
            .then((response) => {
              if (response.data.code == 1) {
                this.$message.success("登录成功！");
                window.sessionStorage.setItem("username", response.data.username);
                router.push("/home");
              } else {
                this.$message.error("用户名或密码错误！");
              }
            });
        }
      });
    },
  },
};
</script> -->

<style scoped>
.login-main {
  
  height: 100vh;
}
.login-form {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.login-form .el-input {
  width: 300px;
}
</style>
