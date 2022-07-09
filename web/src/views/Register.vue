<template>
  <div class="register-form">
    <el-form
      ref="registerFormRef"
      :rules="rules"
      label-width="80px"
      :model="registerForm"
    >
      <el-form-item label="用户名" prop="username">
        <el-input v-model="registerForm.username" placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input
          v-model="registerForm.password"
          type="password"
          placeholder="请输入密码"
          show-password
        />
      </el-form-item>
      <el-form-item label="确认密码" prop="passwordConfirm">
        <el-input
          v-model="registerForm.passwordConfirm"
          type="password"
          placeholder="请确认密码"
          show-password
        />
      </el-form-item>
      <div style="text-align: center">
        <el-button type="danger" @click="register(registerFormRef)">注册</el-button>
        <el-button @click="goback()">返回</el-button>
      </div>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref, getCurrentInstance } from "vue";
import type { FormInstance } from "element-plus";
import { useRouter } from "vue-router";

let { proxy } = getCurrentInstance();

const router = useRouter();

const registerFormRef = ref<FormInstance>();

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

const checkPasswordConfirm = (rule: any, value: any, callback: any) => {
  if (!value) {
    return callback(new Error("请输入密码"));
  } else if (value != registerForm.password) {
    return callback(new Error("密码不一致"));
  } else {
    // 满足规则执行回调函数
    callback();
  }
};

const registerForm = reactive({
  username: "",
  password: "",
  passwordConfirm: ""
});

const rules = reactive({
  username: [{ validator: checkUsername, trigger: "blur" }],
  password: [{ validator: checkPassword, trigger: "blur" }],
  passwordConfirm: [{ validator: checkPasswordConfirm, trigger: "blur" }],
});

const register = (registerFormRef) => {
  registerFormRef.validate(async (valid) => {
    if (valid) {
      await proxy.axios.post("http://"+ document.domain +":8000/register", {
          username: registerForm.username,
          password: registerForm.password,
        })
        .then((response) => {
          if (response.data.code == 1) {
            proxy.$message.success("注册成功！");
            router.back();
          } else {
            proxy.$message.error("用户已存在！");
          }
        });
    }
  });
};


const goback = () => {
    router.back();
}
</script>


<!-- <script lang="ts">
export default {
  name: "AdminIndex",
  methods: {
    register() {
      this.registerFormRef.validate(async (valid) => {
        if (valid) {
          await this.axios
            .post("http://wuud.fun:8000/register", {
            // .post("/register", {
              username: this.registerForm.username,
              password: this.registerForm.password,
            })
            .then((response) => {
              if (response.data.code == 1) {
                this.$message.success("注册成功！");
                router.push('/login');
              } else {
                this.$message.error("用户已存在！");
              }
            });
        }
      });
    },
  },
};
</script> -->

<style scoped>
.register-form {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.register-form .el-input {
  width: 300px;
}
</style>
