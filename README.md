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