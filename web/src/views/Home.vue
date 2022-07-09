<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="300px">
        <h3>WEWO</h3>
        <!-- <h4>Hello! {{this.username}}&#127773;</h4> -->
        <h4>
          Hello! {{ this.username }}&#128517;
          <el-link type="warning" @click="logout">注销</el-link>
        </h4>

        <div class="container-card">
          <span class="span-total"> 笔记数：{{ total }}</span>
        </div>
        <br />
        <span class="span-total" v-show="this.tagitems.length > 0">标签：</span>
        <div class="flex flex-wrap gap-2 my-2">
          <el-check-tag
            v-for="item in this.tagitems"
            class="mx-1 node-tag"
            :key="item"
            effect="light"
            checked
            @click="chosetag(item)"
          >
            {{ item }}
          </el-check-tag>
        </div>
      </el-aside>
      <el-container>
        <el-header height="220px">
          <el-row :gutter="20">
            <!-- 顶部标签与搜索框 -->
            <el-col :span="8" class="head-tag">
              <span class="mx-1"
                >WEWO
                <el-icon :size="18" @click="refresh" style="cursor: pointer">
                  <Refresh /> </el-icon
              ></span>
            </el-col>
            <el-col :span="4"></el-col>
            <el-col :span="4"></el-col>
            <el-col :span="8">
              <el-input
                v-model="searchinput"
                class="w-50 m-2"
                placeholder="search"
                :prefix-icon="Search"
                clearable
              />
            </el-col>
          </el-row>
          <br />
          <!-- <v-md-editor v-model="headerinputext" height="200px"></v-md-editor> -->
          <!-- 新增文本的编辑框 -->
          <!-- 添加本地图片需要把这个加入vmdeditor中  disabled-menus="[]" -->
          <v-md-editor
            v-model="this.edittext"
            ref="inputRef"
            height="150px"
            mode="edit"
            left-toolbar="bold italic ul ol image "
            right-toolbar=" "
            @upload-image="handleUploadImage"
            disabled-menus="[]"
            autofocus
          ></v-md-editor>
          <div style="position:relative;" >
              <div style="position:absolute; top:0px; left:0px;">
                <el-tag
                  :key="this.tag_name"
                  class="mx-1 filterTagShow"
                  closable
                  @close="closetag()"
                  v-if="tag.show"
                  
                >
                  {{ this.tag.tag_name }}
                </el-tag> 
              </div>

              <div style="position:absolute; top:0px; right:0px;">
                  <el-button
                    type="primary"
                    size="small"
                    @click="savenote"
                    style="margin-top: 5px;"
                    >发送</el-button
                  >
              </div>
          </div>
        </el-header>
        <el-main>
          <ul
            v-infinite-scroll="load"
            class="infinite-list"
            style="overflow: auto"
          >
            <li
              v-for="item in filteredNote"
              :key="item.id"
              class="infinite-list-item"
            >
              <el-row :gutter="0">
                <el-col :span="22">
                  <div>
                    <!-- 时间 -->
                    <p
                      class="item-p"
                      style="cursor: pointer"
                      @click="showdetail(item)"
                    >
                      {{ item.update_time }}
                    </p>
                    <!-- 内容预览 -->
                    <v-md-preview
                      class="item-content"
                      :text="highlightTag(item.content)"
                    >
                    </v-md-preview>
                    <!-- 标签展示 -->
                    <el-row>
                      <p class="item-foot">标签:</p>
                      <el-link
                        class="tag-link"
                        v-for="tagitem in item.tags"
                        :key="tagitem"
                        type="success"
                        @click="chosetag(tagitem)"
                      >
                        {{ tagitem }}
                      </el-link>
                    </el-row>
                    <el-row>
                      <p class="item-foot">引用:</p>
                      <el-link
                        class="tag-link"
                        v-for="tagitem in item.links"
                        :key="tagitem"
                        type="primary"
                        @click="handlelink(tagitem)"
                      >
                        {{ tagitem }}
                      </el-link>
                    </el-row>
                  </div>
                </el-col>
                <el-col :span="2">
                  <div>
                    <el-button type="info" size="small" text> </el-button>
                    <el-button
                      type="info"
                      size="small"
                      text
                      @click="showdetail(item)"
                      >详情
                    </el-button>
                    <el-button
                      type="success"
                      size="small"
                      text
                      @click="copynote(item.note_id)"
                      >复制
                    </el-button>
                    <el-button
                      type="primary"
                      size="small"
                      text
                      @click="editnote(item)"
                      >编辑
                    </el-button>
                    <el-button
                      type="danger"
                      size="small"
                      text
                      @click="deletenote(item.note_id)"
                      >删除
                    </el-button>
                    <!-- <el-link type="info"  plain @click="showdetail(item.note_id)">详情</el-link>
                    <el-link type="success"  plain @click="copynote(item.note_id)">复制</el-link>
                    <el-link type="primary" plain @click="editnote(item)">编辑</el-link>
                    <el-link type="danger"  plain @click="deletenote(item.note_id)">删除</el-link> -->
                  </div>
                </el-col>
              </el-row>
            </li>
          </ul>
        </el-main>
      </el-container>
      <!-- 编辑抽屉 -->
      <el-drawer v-model="dialog" direction="rtl" custom-class="demo-drawer">
        <div class="demo-drawer__content">
          <v-md-editor
            v-model="this.onedit"
            height="300px"
            mode="edit"
            left-toolbar="bold italic ul ol image "
            right-toolbar=" "
            @upload-image="handleUploadImage"
            disabled-menus="[]"
            autofocus
          ></v-md-editor>
          <br />
          <el-row :gutter="20">
            <el-col :span="6"></el-col>
            <el-col :span="14"></el-col>
            <el-col :span="3" style="padding-right=10px">
              <el-button type="primary" @click="saveeditnote">保存</el-button>
            </el-col>
          </el-row>
          <br />
        </div>
      </el-drawer>

      <!-- 详情抽屉 -->
      <el-drawer
        v-model="detaildialog"
        title="笔记详情"
        direction="rtl"
        custom-class="demo-drawer"
        :before-close="handleDetailClose"
      >
        <div class="demo-drawer__content">
          <!-- for item in detailnotes     detailnotes 应该和allData.notes  格式一样
            然后 用v-md-editor li   逐个渲染 -->
          <ul
            v-infinite-scroll="load"
            class="infinite-list-drawer"
            style="overflow: auto"
          >
            <li
              v-for="item in topDetailNote"
              :key="item.id"
              class="infinite-list-item"
            >
              <el-row :gutter="0">
                <el-col :span="22">
                  <div>
                    <!-- 时间 -->
                    <p
                      class="item-p"
                      style="cursor: pointer"
                      @click="showdetail(item)"
                    >
                      {{ item.update_time }}
                    </p>
                    <!-- 内容预览 -->
                    <v-md-preview
                      class="item-content"
                      :text="highlightTag(item.content)"
                    >
                    </v-md-preview>
                    <!-- 标签展示 -->
                    <!-- <el-row>
                      <p class="item-foot">标签:</p>
                      <el-link
                        class="tag-link"
                        v-for="tagitem in item.tags"
                        :key="tagitem"
                        type="success"
                      >
                        {{ tagitem }}
                      </el-link>
                    </el-row> -->
                    <el-row>
                      <p class="item-foot">引用:</p>
                      <el-link
                        class="tag-link"
                        v-for="tagitem in item.links"
                        :key="tagitem"
                        type="primary"
                        @click="handlelink(tagitem)"
                      >
                        {{ tagitem }}
                      </el-link>
                    </el-row>
                  </div>
                </el-col>
                <el-col :span="2">
                  <div>
                    <!-- <el-button type="info" size="small" text> </el-button>
                    <el-button
                      type="info"
                      size="small"
                      text
                      @click="showdetail(item)"
                      >详情
                    </el-button> -->
                    <el-button
                      type="success"
                      size="small"
                      text
                      @click="copynote(item.note_id)"
                      >复制
                    </el-button>
                    <!-- <el-button
                      type="primary"
                      size="small"
                      text
                      @click="editnote(item)"
                      >编辑
                    </el-button> -->
                    <!-- <el-button
                      type="danger"
                      size="small"
                      text
                      @click="deletenote(item.note_id)"
                      >删除
                    </el-button> -->
                    <!-- <el-link type="info"  plain @click="showdetail(item.note_id)">详情</el-link>
                    <el-link type="success"  plain @click="copynote(item.note_id)">复制</el-link>
                    <el-link type="primary" plain @click="editnote(item)">编辑</el-link>
                    <el-link type="danger"  plain @click="deletenote(item.note_id)">删除</el-link> -->
                  </div>
                </el-col>
              </el-row>
            </li>
          </ul>

          <p class="item-p-link">引用的wewo:</p>

          <ul
            v-infinite-scroll="load"
            class="infinite-list-drawer"
            style="overflow: auto"
          >
            <li
              v-for="item in detailNote"
              :key="item.id"
              class="infinite-list-item"
            >
              <p class="item-p">#{{ item.note_id }}</p>
              <el-row :gutter="0">
                <el-col :span="22">
                  <div>
                    <!-- 时间 -->
                    <p
                      class="item-p"
                      style="cursor: pointer"
                      @click="showdetail(item)"
                    >
                      {{ item.update_time }}
                    </p>
                    <!-- 内容预览 -->
                    <v-md-preview
                      class="item-content"
                      :text="highlightTag(item.content)"
                    >
                    </v-md-preview>
                    <!-- 标签展示 -->
                    <!-- <el-row>
                      <p class="item-foot">标签:</p>
                      <el-link
                        class="tag-link"
                        v-for="tagitem in item.tags"
                        :key="tagitem"
                        type="success"
                      >
                        {{ tagitem }}
                      </el-link>
                    </el-row> -->
                    <el-row>
                      <p class="item-foot">引用:</p>
                      <el-link
                        class="tag-link"
                        v-for="tagitem in item.links"
                        :key="tagitem"
                        type="primary"
                        @click="handlelink(tagitem)"
                      >
                        {{ tagitem }}
                      </el-link>
                    </el-row>
                  </div>
                </el-col>
                <el-col :span="2">
                  <div>
                    <el-button type="info" size="small" text> </el-button>
                    <el-button
                      type="info"
                      size="small"
                      text
                      @click="showdetail(item)"
                      >详情
                    </el-button>
                    <el-button
                      type="success"
                      size="small"
                      text
                      @click="copynote(item.note_id)"
                      >复制
                    </el-button>
                    <!-- <el-button
                      type="primary"
                      size="small"
                      text
                      @click="editnote(item)"
                      >编辑
                    </el-button> -->
                    <!-- <el-button
                      type="danger"
                      size="small"
                      text
                      @click="deletenote(item.note_id)"
                      >删除
                    </el-button> -->
                    <!-- <el-link type="info"  plain @click="showdetail(item.note_id)">详情</el-link>
                    <el-link type="success"  plain @click="copynote(item.note_id)">复制</el-link>
                    <el-link type="primary" plain @click="editnote(item)">编辑</el-link>
                    <el-link type="danger"  plain @click="deletenote(item.note_id)">删除</el-link> -->
                  </div>
                </el-col>
              </el-row>
            </li>
          </ul>
          <br />
        </div>
      </el-drawer>
    </el-container>
  </div>
</template>

<script>
import { ref } from "vue";
import { Search, Delete, Edit } from "@element-plus/icons-vue";
import { Axios } from "axios";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      router: useRouter(),
      Search,
      Delete,
      Edit,
      inputfocus: true,
      username: window.sessionStorage.getItem("username"),
      selectedlabel: "WEWO",
      //搜索内容标签
      searchinput: "",
      //头部选择的标签
      tag: {
        tag_name: "",
        show: false,
      },
      // 新增的笔记内容，tag
      edittext: "",

      //全部笔记内容
      notes: [],
      //全部标签
      tagitems: "",
      //  在编辑的内容
      onedit: "",
      // ontag:"",
      onid: "",
      //  编辑框
      dialog: false,
      // showedit:fasle,
      // 详情框
      detaildialog: false,
      detailNote: [],
      topDetailNote: [],
    };
  },
  created() {
    // getnotes()
    // 获取全部数据
    this.getAllData();
  },
  computed: {
    total() {
      return this.notes.length;
    },
    //筛选展示的笔记
    filteredNote() {
      return this.notes.filter((data) => {
        if (this.searchinput === "" && this.tag.tag_name === "") return true;
        if (this.searchinput != "" && !data.content.includes(this.searchinput))
          return false;
        if (
          this.tag.tag_name != "" &&
          data.tags.indexOf(this.tag.tag_name) == -1
        )
          return false; //要改成 data.tags数组不包含this.tag.tag_name
        return true;
      });
    },

    //笔记的数量
    count() {
      return this.notes.length;
    },
  },
  methods: {
    async getAllData() {
      var url = "http://"+ document.domain +":8000/home";
      await this.axios
        .get(url, {
          params: {
            username: this.username,
          },
        })
        .then((response) => {
          // console.log(response.data);
          this.notes = response.data.notes;
          this.tagitems = response.data.total_tags;
        });
    },
    refresh() {
      this.getAllData();
    },
    logout() {
      window.sessionStorage.clear();
      this.router.push("/login");
    },
    // 关闭筛选tag
    closetag() {
      this.tag.tag_name = "";
      this.tag.show = false;
      this.edittext = "";
      this.$refs.inputRef.focus();
    },
    // 选择tag
    chosetag(chosedtag) {
      this.tag.tag_name = chosedtag;
      this.edittext = "#" + chosedtag + " ";
      this.tag.show = true;
      this.$refs.inputRef.focus();
    },
    //  载入加载数据
    load() {
      this.count += 0;
    },
    //  处理上传图片
    async handleUploadImage(event, insertImage, files) {
      // 拿到 files 之后上传到文件服务器，然后向编辑框中插入对应的内容
      // console.log("files[0]");
      // console.log(files[0]);

      let formData = new FormData();
      formData.append("file", files[0]);
      // console.log("formData:");
      // console.log(formData);
      let picurl = "";
      await this.axios(
        
        {
          method: "post",
          url: "http://"+ document.domain +":8000/image/add",
          data: formData,
          params: {
            username: "test1",
          },
        }
      ).then((response) => {
        // console.log(response);
        picurl = "http://"+ document.domain +":8000/image" + response.data.url;
      });
      // console.log(picurl);
      let picdesc = this.username + "的图片";
      insertImage({
        url: picurl,
        desc: picdesc,
        width: "auto",
        height: "auto",
      });
    },

    //  保存笔记     post 给 后台   然后  刷新  重新获取笔记列表
    async savenote() {
      if (this.edittext == "") return;
      var posttext = this.edittext;
      await this.axios({
        method: "post",
        url: "http://" +document.domain+ ":8000/note/add",
        data: {
          content: posttext,
          username: this.username,
        },
        params: {
          username: this.username,
        },
      }).then((response) => {
        if (response.data.code == 1) {
          // console.log("添加成功");
          this.getAllData();
        }
      });
      //  getnotes();
      this.edittext = "";
    },
    // 复制笔记 获取链接
    copynote(noteid) {
      // 模拟 输入框
      var cInput = document.createElement("input");
      cInput.value = "link://note/" + noteid + " ";
      document.body.appendChild(cInput);
      cInput.select(); // 选取文本框内容

      // 执行浏览器复制命令
      // 复制命令会将当前选中的内容复制到剪切板中（这里就是创建的input标签）
      // Input要在正常的编辑状态下原生复制方法才会生效

      document.execCommand("copy");

      this.$message({
        type: "success",
        message: "已复制笔记链接",
      });
      // 复制成功后再将构造的标签 移除
      document.body.removeChild(cInput);
    },
    //   点击编辑按钮触发  编辑笔记抽屉弹出
    editnote(editednote) {
      this.onedit = editednote["content"];
      this.onid = editednote["note_id"];
      //弹出编辑框
      this.dialog = true;
    },
    async saveeditnote() {
      // post({onedit, onid})     把要修改内容的笔记id 和新内容传送给 服务器   服务器修改后，返回新的
      // console.log(this.onid);
      // console.log(this.onedit);
      await this.axios({
        method: "post",
        url: "http://"+document.domain+":8000/note/" + this.onid,
        data: {
          content: this.onedit,
          username: this.username,
        },
        params: {
          username: this.username,
        },
      }).then((response) => {
        // console.log(response);
        if (response.data.code == "1") {
          this.$message.success("修改成功");
          this.getAllData();
          this.onedit = "";
          this.onid = "";
          this.dialog = false;
        } else {
          this.$message.error(response.data.message);
        }
      });
    },
    async deletenote(deletenoteid) {
      // console.log(deletenoteid);
      //  post给后端  要删除的笔记的id    删除后  获取新的
      //  getnotes();
      // console.log(deletenoteid);
      await this.axios({
        method: "post",
        url: "http://"+document.domain+":8000/note/delete",
        data: {
          note_id: deletenoteid,
          username: this.username,
        },
        params: {
          username: this.username,
        },
      }).then((response) => {
        // console.log(response);
        if (response.data.code == "1") {
          this.$message.success("删除成功");
          // this.getAllData();
          this.notes = this.notes.filter((item) => {
            return item.note_id != deletenoteid;
          });
        }
      });
    },
    //  查看笔记详情
    async showdetail(note) {
      //   postnodeid  获取   该笔记的全部链接      链接是url?  nonono    应该是  data
      //   点击后读取 笔记id   更新detailNote
      this.detailNote = [];
      this.topDetailNote = [];
      var lists = note.links;
      this.topDetailNote.push(note);

      for (var i = 0; i < this.notes.length; i++) {
        // console.log("this.notes[" + i + "].note_id:");
        // console.log(this.notes[i].note_id);
        for (var j = 0; j < lists.length; j++) {
          if (lists[j] == this.notes[i].note_id) {
            this.detailNote.push(this.notes[i]);
          }
        }
      }
      this.detaildialog = true;
    },
    handleDetailClose() {
      this.detailNote = [];
      this.topDetailNote = [];
      this.detaildialog = false;
    },
    
    async handlelink(linknote_id) {
      this.detailNote = [];
      this.topDetailNote = [];
      await this.axios({
        method: "get",
        url: "http://"+document.domain+":8000/note/" + linknote_id,
        params: {
          username: this.username,
        },
      }).then((response) => {
        // console.log(response);
        if (response.data.code == "1") {
          this.showdetail(response.data.main_note);
        }
      });
    },

    highlightTag(text) {
      text = text

        .replace(
          /#\S+/g,
          (match) =>
            "<a href=' " +
            match.slice(1) +
            "/' style='pointer-events:none;'><span class='tag'>" +
            match +
            "</span></a>"
        )
        .replace(
          /link:\/\/note\/[0-9]+/g,
          (match) =>
            "<a href='#' style='pointer-events:none;'><span class='link'>Wewo</span></a>"
        );
      return text;
    },
  },
};
</script>



<style>
.tag {
  background-color: #00e09e;
  color: #f2fdff;
}

.link {
  font-weight: bold;
  color: #2e4e7e;
  background-color: #e0f0e9;
}

.common-layout {
  margin: 0 300px;
}

h3 {
  font-size: 1.75rem;
  font-weight: 700;
  line-height: 1.75rem;
}

.head-tag {
  /* vertical-align: center; */
  font-weight: bold;
  font-size: 22px;
}

.span-total {
  font-size: 1.125rem;
  font-weight: 700;
  line-height: 1.75rem;
  vertical-align: text-bottom;
}

.filterTagShow {
  margin: 5px 5px 5px 0;
}

.infinite-list {
  height: 661px;
  padding: 0;
  margin: 0;
  list-style: none;
}
.infinite-list .infinite-list-item {
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: center; */
  /* height: 100px; */
  /* background: var(--el-color-primary-light-9); */
  margin: 10px 0;
  /* color: var(--el-color-primary); */
  background: whitesmoke;
  border-radius: 0.5rem;
}

.infinite-list .infinite-list-item + .list-item {
  margin-top: 10px;
}
.infinite-list-drawer {
  /* height: 630px; */
  padding: 0;
  margin: 0;
  list-style: none;
}
.infinite-list-drawer .infinite-list-item {
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: center; */
  /* height: 100px; */
  /* background: var(--el-color-primary-light-9); */
  margin: 10px 0;
  /* color: var(--el-color-primary); */
  background: whitesmoke;
  border-radius: 0.5rem;
}

.infinite-list-drawer .infinite-list-item + .list-item {
  margin-top: 10px;
}

.infinite-list-item {
  padding: 16px;
}

.item-p {
  margin: 0;
  font-size: 12px;
  color: #8f9193;
  /* text-align: center; */
}
.item-p-link {
  margin: 5px;
  font-size: 14px;
  color: #8f9193;
}
.item-foot {
  margin: 0 2px;
  padding: 0 2px;
  font-size: 12px;
  color: #8f9193;
  line-height: 24px;

  /* text-align: center; */
}

div.github-markdown-body {
  padding: 16px 0;
}

.node-tag {
  padding: 5px;
  margin: 5px 5px 5px 0;
}

/* .tag-link {
    display:block;
    padding: 0;
    margin: 0,10px;
} */
.el-link {
  margin-right: 8px;
  /* pointer-events:none; */
}

.el-link .el-icon--right.el-icon {
  vertical-align: text-bottom;
}

/* .el-link__inner {
    padding: 0;
    margin: 0,10px;
} */
</style>