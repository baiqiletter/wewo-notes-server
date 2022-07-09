import { createApp } from "vue";
import ElementPlus from "element-plus";
import 'element-plus/dist/index.css';
import axios from 'axios';
import VueAxios from 'vue-axios';
import App from "./App.vue";
import router from "./router";
// 统一导入el-icon图标
import * as ElIconModules from '@element-plus/icons'
//  轻量版
import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';
import Prism from 'prismjs';
VueMarkdownEditor.use(vuepressTheme, {
  Prism,
});
//   预览版
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
// highlightjs
import hljs from 'highlight.js';
VMdPreview.use(githubTheme, {
  Hljs: hljs,
});

import VMdPreviewHtml from '@kangc/v-md-editor/lib/preview-html';
import '@kangc/v-md-editor/lib/style/preview-html.css';
// import '@kangc/v-md-editor/lib/theme/style/vuepress';


const app = createApp(App);

// use
app.use(ElementPlus);
app.use(router);
app.use(VueAxios, axios);
axios.defaults.baseURL = "/api"
app.use(VueMarkdownEditor);
app.use(VMdPreview);
app.use(VMdPreviewHtml);
// 统一注册el-icon图标
for(let iconName in ElIconModules){
    app.component(iconName,ElIconModules[iconName])
}

app.mount("#app");
