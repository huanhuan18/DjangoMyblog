### 52.开始项目，数据库设计
	1>新建项目 django-admin startproject xxx(mysite)
	2>新建app python manage.py startapp xxx(myblog)
	3>数据库迁移 
		python manage.py makemigrations //具体在某个应用下更新可在后面加上app名称,如myblog
		python manage.py migrate
	4>运行Django python manage.py runserver 127.0.0.1:9000
	5>在models.py中写入数据表
		User是django提供的，然后为了管理这些用户再创建一个一对一的用户Userinfo（头像，昵称，OneToOneField(User)）表
	6>再分别创建表：文章Article （标题，封面，文本，一对多所属用户ForeignKey(Userinfo)）  //一个用户有多篇文章
					收藏Favorite（外键所属用户ForeignKey(Userinfo)，外键所属文章ForeignKey(Article)）
					点赞Like    （外键所属用户ForeignKey(Userinfo)，外键所属文章ForeignKey(Article)）
					打赏PayOrder（订单号，价格，状态）
					分类Category（名称，外键所属自身ForeignKey(self)） //查询所属父级个数为0时，就可以认为是顶层栏目
### 54.引入elementUI
	1>终端输入vue ui,选择目录创建项目,添加vue-router,vuex,element-ui
	2>在main.js内引入import ElementUI from 'element-ui'    //不过最好是按需引入
					 import 'element-ui/lib/theme-chalk/index.css';
					 Vue.use(ElementUI)
	3><el-switch v-model="value" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
		data() {
		  return {
			value: true
		  }
### 55.布局整站样式css
	assets/css/mystyle.css
### 56.响应式布局
	1>引入element中的class="el-icon-menu"的图标，修改样式#left-menu #left-btn {...}
	2>修改属性xs,绑定给data中的mobile_left和changeDevice、showHideLeftMenu方法实现侧边栏的收缩
	3>绑定element的响应式布局xs和lg给content-menu,添加mobile_content的class
### 57.添加导航栏，引入表单
	1>从elementUI中复制一个自定义导航栏组件<el-col>然后修改样式  //任意6个数字再加2个0为透明色
	2>在mystyle.css中的其他注释中修改组件的样式
	3>添加路由'/add-article'，并新建组件AddArticle.vue
	4>给导航栏第一项的子选项添加一个路由跳转方法toAddArticle，然后去编辑AddArticle.vue
### 58.引入富文本（jquery与bootstrap的webpack引入）
	summernote官网：https://summernote.org/getting-started/
	1>在开发依赖里安装jquery、bootstrap@4.5.0、summernote、popper.js@1.16.0   //版本要对
	2>在main.js内mystyle.css上方引入summernote
		import 'bootstrap'
		import 'bootstrap/dist/css/bootstrap.css'
		import 'popper.js'
		import 'summernote'
		import 'summernote/dist/summernote.css'
	3>在AddArticle.vue中写入
		<div id="summernote">Hello Summernote</div>
		mounted() {
			this.summernote()
		},
		methods: {
			summernote() {
				$('#summernote').summernote();
			}
		},    //即可看到富文本样式
	4>修改富文本样式  在mystyle.css中修改class -> note-btn、dropdown-menu、popover、note-editable
	5>在main.js中导入富文本中文语言包import 'summernote/lang/summernote-zh-CN.js', 然后在AddArticle.vue中使用lang:'zh-CN'
		因为该js导入的jquery语法不能在这用，所以将顶部删去，用summernote包下的src/js/base/summernote-en-US.js的头部代替
### 59.配置应用框架组件（学会查阅文档）
	1>将App.vue中的发布文章的toAddArticle方法删掉，改为index="/add-article"
	2>在el-menu标签中加入属性router  //可以从组件文档中找到该属性，它的返回值是boolean,写上就代表开启路由跳转
	自己写的push路由和组件自带的路由会产生一个bug->重复点击会报错
	3>在index.js中引用VueRouter之前加入配置  //在3.1.0+以后已经修复，不需要此步骤
	4>测试文档中select事件，在el-menu标签中加入@select="ChooseMenu"
		ChooseMenu(index) {
		  console.log(index)   //index是select事件的回调参数
		  // this.$router.push({path:index})  //关掉el-menu的router可启用该句
		},
### 60.文章发布页-富文本图片插入
	1>调整布局，将input改为多行文本type="textarea"，修改样式.el-textarea__inner
	2>添加success按钮，修改位置，并将summernote宽度铺满width:'100%'
	3>在summernote内加入回调函数onChange、onImageUpload
	4>使用组件中的image图片el-image可以修改展示的样式，注意:fit="'cover'"绑定的是字符串
### 61.文章发布页-远程图片插入
	1>onImageLinkInsert，用法与本地图片插入相同
### 62.文章发布页-封面图选定
	1>监听删除图片方法onMediaDelete()
	2>写onChange方法， 修改.dweb .el-image:hover样式
	3>在el-image标签上加上@click="chooseCover(img)
### 63.后端：服务搭建与api文档书写
	1>监听保存文章的点击方法submitArticle
	2>安装axios模块，导入import axios from 'axios'
	3>配置后端settings和url
	4>pip install djangorestframework
	  pip install django-cors-headers
	5>修改models.py，迁移数据库python manage.py makemigrations
		python manage.py migrate
		python manage.py runserver 127.0.0.1:9000
	6>创建超级用户python manage.py createsuperuser
	7>把Article表注册到admin.py中
	8>在blog下新建api_url.py，然后在urls.py中配置path('api/', include(api_url)),以后api之后的路由都在api_url.py中写
	8>在blog下新建api.py,在里面写视图函数
		from rest_framework.response import Response
		from rest_framework.decorators import api_view

		@api_view(['POST'])
		def add_article(request):
			return Response('ok')
	9>在settings.py中添加跨域配置
	10>书写api文档  apipost/swagger   //个人token  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
		pip install drf-yasg2
		更新项目文件里的 settings.py 来加载 drf_yasg2 
			INSTALLED_APPS = ['drf_yasg2']
		更新项目里的 urls.py 文件来加载 the schema_view
			# drf_yasg2 从这里开始
			from rest_framework import permissions
			from drf_yasg2.views import get_schema_view
			from drf_yasg2 import openapi
			schema_view = get_schema_view(
				openapi.Info(
					title="Tweet API",
					default_version='v1',
					description="Welcome to the world of Tweet",
					terms_of_service="https://www.tweet.org",
					contact=openapi.Contact(email="demo@tweet.org"),
					license=openapi.License(name="Awesome IP"),
				),
				public=True,
				permission_classes=(permissions.AllowAny,),
			)
			urlpatterns = [
				re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- 这里
				path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  #<-- 这里
				path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  #<-- 这里
			]
### 64.Python爬虫利器 Beautiful
	1>点击保存文章按钮在审查元素界面->Network->XHR->请求中可以看到传入的四个字段，然后在后端中获取它
	2>在api.py中直接获取title会发现500报错，这时需要将传入的字段格式化
	3>在AddArticle.vue中添加import Qs from 'qs'
		axios.post('http://127.0.0.1:9000/api/add-article/',Qs.stringify(article_data))，此时可正确获取到title字段
	4>安装beautofulsoup  pip install beautifulsoup4并导入from bs4 import BeautifulSoup
		soup = BeautifulSoup(content, 'html.parser')
		imgList = soup.find_all('img')
		print(imgList[0]['src'])
	5>导入requests
### 65.保存远程图片（下载）
	1>image = requests.get(src)  # 请求远程图片
	2>from PIL import Image
	  from io import BytesIO
	  image_data = Image.open(BytesIO(image.content))  # 转化为二进制
	3>image_data.save('upload/' + image_name + '.png')
	//示例远程图片  https://www.dweb.club/img/logo.d58a9d80.png
### 66.保存本地图片（上传）
	1>import base64
	  image_data = base64.b64decode(src.split(',')[1])   //将二进制通过base64变成可操作的
	2>把图片二进制写入一个文件with open(image_url, 'wb') as f:
								f.write(image_data)
	3>保存一个文章的所有字段
		new_article = Article(title=title)
		new_article.content = content
		new_article.describe = describe
		new_article.cover = cover
		new_article.save()
		
	//0901个人token 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
	git remote set-url origin https://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@github.com/huanhuan18/mywork.git
### 67.用户管理 登录注册api接口
	1>在settings.py中的INSTALLED_APPS中加入'rest_framework.authtoken',
	2>执行数据表迁移python manage.py migrate
	3>编辑models.py中的Userinfo表，然后继续制作数据库并迁移
	4>将Userinfo表加入到admin.py中，方便在admin中可以看到
	5>在api_url.py中写两个接口api.gf_login和api.gf_register，并在api.py中添加对应的函数
	6>在api.py中导入django自带的User表和Token表
		from django.contrib.auth.models import User
		from rest_framework.authtoken.models import Token
		from django.contrib.auth.hashers import check_password, make_password
### 68.前端：登录注册页 Api接通传递Token
	1>在index.js中添加登录和注册路由，并在views下新建两个vue文件
	2>编辑Login.vue和Register.vue(superuser:gf123, gaofei123)
	3>将2中获取到的token存入vuex内管理
		在store下的index.js内编辑state（相当于data）和mutations(相当于methods,官方文档中说明了state只能由mutations修改)
		在Login.vue和Register中使用，例如this.$store.commit('saveUserinfo', res.data)  //第一个参数是方法，第二个是该方法需要传入的数据
	4>查看vuex中的状态->在vue ui的依赖下安装vue devtools插件
### 69.vuex管理异步请求 actions的方法写入与使用
	1>在store下的index.js内编辑actions,将ajax请求放到vuex中统一管理
	2>修改登录注册中原先的调用方法为this.$store.dispatch("blogLogin", this.formData); //dispatch就是调用actions中的方法
### 70.路由鉴权与路由守卫
	1>在index.js中的路由下添加
		beforeEnter: (to, from, next) => {
		  if (store.state.userinfo.token) {
			next()
		  }else{
			next('/login')
		  }
		}
		设置路由守卫报错Redirected when going from "/1-2" to "/add-article" via a navigation guard.
		解决：将版本vue-router版本降到3.0.7（npm uninstall vue-router;   npm install vue-router@3.0.7）
	2>在index.js内定义全局路由
		router.beforeEach((to,from,next)=>{})   //注意要在定义const router下面用，否则会报错undefined
	3>在Login.vue中定义局部路由
		beforeRouteEnter (to, from, next) {}
### 71.登录状态修改UI
	1>在store下的index.js中的登录和注册成功后加入router.push({path:'/'})
	2>getters去集合查询state中的各种信息，在里面写入方法isnotUserlogin(state)
	3>使用computed  //同data,区别是data中只能是对象，但是computed里面可以是方法，在里面加入authUserLogin方法
	4>在App.vued的 退出登录的标签上加上v-if="authUserLogin"，这样在未登录状态时就不展示退出登录
	5>在store下的index.js中的mutations里加入clearUserinfo方法
	6>在App.vued的 退出登录的标签上加上blogLogout()方法
	7>将登出方法也写到在store下的index.js中的actions里面，方便管理，在App.vue中this.$store.dispatch('blogLogout')这样去调用它
### 72.自动登录与token重置
	1>watch用来监听方法的变化，在App.vue中加入watch监听authUserLogin方法
	2>登录注册成功之后就在本地缓存token    //localStorage.setItem('token',res.data.token)
	3>自动登录原理：刷新时调取缓存中的token   //localStorage.getItem('token')  然后post给后端获得用户信息
		实现：先在store下的index.js中的actions写入tryAutoLogin方法，
			  然后在App.vue中的created生命周期内执行该函数，这个生命周期比mounted早一点，在它之前
			  然后在后端添加自动登录的路由auto-login和获取token的方法gf_autoLogin	
			  然后在actions中的自动登录方法内加入登录的逻辑（保存token）
	4>在actions中的登出方法内点击退出登录就删除token    //localStorage.removeItem('token')
	5>重置token原理：点击退出登录的那一刻将token发送到后端，然后删掉该token，下一次再登录就重新获取
		实现：修改actions中的blogLogout方法
			  然后在后端添加对应的路由和函数
			  最后在App.vue中的登出方法中传入token参数   //this.$store.dispatch('blogLogout',this.$store.getters.isnotUserlogin)
	6>优化自动登录：在不同设备（localhost和局域网ip）中退出登录删除token之后另一设备提示token过期
### 73.文章列表页与前端分页器
	1>编写文章列表页，现在views里添加ArticleList.vue，并在index.js内分配路由，然后在App.vue中的文章列表标签上加上路由
	2>编辑ArticleList.vue,在mystyle.css中修改文章列表页的面包屑样式
	  相对路径图片绑定  <el-image :src="require('../assets/img/article1.png')"></el-image>
	3>将App.vue中的screenWidth传给子组件<router-view :screenWidth="screenWidth"></router-view>，子组件中props:['screenWidth']获取继续编辑
	4>添加分页器
### 74.列表分页交互与文章删除
	1.后端导入django自带分页器from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
	2.可以通过这种方式将增删改查方法写在一个路由里面
		@api_view(['GET','DELETE])
			def articleList(request):
				if request.methos=='DELETE':
					xxx
	3.执行删除操作时要在axios中加入，否则会415报错
		headers:{
          "Content-Type": "application/x-www-form-urlencoded",
        }
	4.浏览器自带的删除验证提示框if (confirm('是否确定删除')){xxx}