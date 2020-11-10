<template>
  <v-card class="v-card-slot" dark :loading="isUpdating">
    <template v-slot:progress>
      <v-progress-linear
        absolute
        color="amber lighten-1"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>

      <v-row>
        <v-col class="text-right" cols="12">
          <v-menu bottom left transition="slide-y-transition">
            <v-list>
              <v-list-item @click="isUpdating = true">
                <v-list-item-action>
                  <v-icon>mdi-cog</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Update</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-col>
        <v-row class="pa-4" align="center" justify="center">
          <v-col class="text-center">
            <h3 class="headline">원하는 결과를 아직 찾지 못했나요?</h3>
          </v-col>
        </v-row>
      </v-row>
    <!-- 여기서부터 폼 시작 -->
    <v-form>
      <v-container>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="country"
              :disabled="isUpdating"
              filled
              color="amber lighten-1"
              label="국가"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="genre"
              :disabled="isUpdating"
              filled
              color="amber lighten-1"
              label="장르"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-autocomplete
              v-model="friends"
              :disabled="isUpdating"
              :items="people"
              filled
              chips
              color="amber lighten-1"
              label="Select"
              item-text="name"
              item-value="name"
              multiple
            >
              <template v-slot:selection="data">
                <v-chip
                  v-bind="data.attrs"
                  :input-value="data.selected"
                  close
                  @click="data.select"
                  @click:close="remove(data.item)"
                >
                  <v-avatar left>
                    <v-img :src="data.item.avatar"></v-img>
                  </v-avatar>
                  {{ data.item.name }}
                </v-chip>
              </template>
              <template v-slot:item="data">
                <template v-if="typeof data.item !== 'object'">
                  <v-list-item-content v-text="data.item"></v-list-item-content>
                </template>
                <template v-else>
                  <v-list-item-avatar>
                    <img :src="data.item.avatar" />
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title
                      v-html="data.item.name"
                    ></v-list-item-title>
                    <v-list-item-subtitle
                      v-html="data.item.group"
                    ></v-list-item-subtitle>
                  </v-list-item-content>
                </template>
              </template>
            </v-autocomplete>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        :loading="isUpdating"
        color="amber"
        depressed
        @click="isUpdating = true"
      >
        <v-icon left> mdi-update </v-icon>
        세부 검색 하기
      </v-btn>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    const srcs = {
      1: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
      2: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
      3: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
      4: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
      5: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
    };

    return {
      friends: ["Sandra Adams", "Britta Holt"],
      isUpdating: false,
      country: "",
      people: [
        { header: "Group 1" },
        { name: "이거는", group: "Group 1", avatar: srcs[1] },
        { name: "나중에 바꿔도 되니까", group: "Group 1", avatar: srcs[2] },
        { name: "데이터가 들어오면", group: "Group 1", avatar: srcs[3] },
        { name: "그때 바꾸자", group: "Group 1", avatar: srcs[2] },
        { divider: true },
        { header: "Group 2" },
        { name: "일단 지금은", group: "Group 2", avatar: srcs[4] },
        { name: "동작이 잘 되니까", group: "Group 2", avatar: srcs[5] },
        { name: "그걸로 만족하고", group: "Group 2", avatar: srcs[1] },
        { name: "다음단계로 고고", group: "Group 2", avatar: srcs[3] },
      ],
      genre: "",
    };
  },

  watch: {
    isUpdating(val) {
      if (val) {
        setTimeout(() => (this.isUpdating = false), 3000);
      }
    },
  },

  methods: {
    remove(item) {
      const index = this.friends.indexOf(item.name);
      if (index >= 0) this.friends.splice(index, 1);
    },
  },
};
</script>