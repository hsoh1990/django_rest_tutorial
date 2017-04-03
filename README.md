## Django REST Framwork
------

**Table of Contents**

- [Python install](#Python install)
- [Virtual Environment](#Virtual Environment)
- [Django install](#Django install)
- [psycopg2 install](#psycopg2 install)
- [Django REST Framwork install](#Django REST Framwork install)
- [Django project 생성](# Django project 생성)
- [Database 연동](#Database 연동)
- [Django REST Framework 사용하기](# Django REST Framework 사용하기)
- [Django_rest_swagger 사용하기](#Django_rest_swagger 사용하기)

### Python install

#### windows
윈도우용 파이썬은 https://www.python.org/downloads/에서 다운 후 설치(PATH 설정은 알아서..)

#### macOS
```brew install python3```으로 설치(확인은 ```python3 --version```)

### Virtual Environment
장고를 설치하기 전에, 개발 환경을 깔끔하게 관리하기 위한 가상환경 구축이 필요하다.
가상 환경(virtualenv)은 프로젝트 기초 전부를 Python/Django와 분리시켜준다. 다시 말해 웹사이트가 변경되어도 개발 중인 것에 영향을 미치지 않는다.
즉, 해당 가상 환경에서 필요한 모듈을 다운받은 경우 다른 가상 환경에서 사용하는 모듈에 영향을 미치지 않는다.

가상 환경을 구축할 디렉토리를 만들고 해당 디렉토리에서 다음 명령을 실행한다.

```bash
$ python -m venv djangovenv
```

가상 환경을 사용하는 방법은 다음과 같다.

```bash
G:\PyCharm\django $ djangovenv/Script/activate
(djangovenv) G:\PyCharm\django $ 
```

### Django install
Python은 pip 명령을 통해 모듈을 설치, 제거한다. Django 모듈설치는 다음과 같다.


```bash
(djangovenv) G:\PyCharm\django $ pip install django

Collecting django
  Using cached Django-1.10.6-py2.py3-none-any.whl
Installing collected packages: django
Successfully installed django-1.10.6
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

해당 메시지가 나오면 모듈 설치 완료

### psycopg2 install
Django에서는 기본적으로 sqlite3를 제공하지만 PostgreSQL를 사용하기 위해서는 psycopg2 모듈 설치해야한다.
```bash
(djangovenv) G:\PyCharm\django $ pip install psycopg2

Collecting psycopg2
  Using cached psycopg2-2.7.1-cp35-cp35m-win32.whl
Installing collected packages: psycopg2
Successfully installed psycopg2-2.7.1
```
모듈을 사용하기 위해서는 Django project에서 설정해야한다. 뒤에 설명한다.

### Django REST Framwork install

```bash
(djangovenv) G:\PyCharm\django $ pip install djangorestframework

Collecting djangorestframework
  Using cached djangorestframework-3.6.2-py2.py3-none-any.whl
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.6.2
```

### Django project 생성
Django 모듈을 설치하면 Django관령 명령을 사용할 수 있다. 프로젝트 생성 명령은 다음과 같이 사용한다.


```bash
(djangovenv) G:\PyCharm\django $ django-admin startproject django_rest_tutorial
```

명령이 수행되면 해당 디렉토리에 django_rest_tutorial라는 프로젝트가 생성된다. 해당 프로젝트로 이동 후 다음 명령을 통해 서버를 구동한다.

```bash
(djangovenv) G:\PyCharm\django $ cd django_rest_tutorial
(djangovenv) G:\PyCharm\django\django_rest_tutorial $ manage.py runserver 
```

기본 포트는 8000번이고 -p 옵션을 통해 변경가능하다. ```http://localhost:8000```으로 접속하여 동작을 확인한다.


#### 파일 설명

1. manage.py

	Django에서 제공하는 명령을 실행하는 파일로 다음과 같은 명령을 수행할 수 있다.
    ```bash
    manage.py startapp <앱이름> 		// 새로운 장고앱 생성
	manage.py runserver 				// 개발 서버 실행
	manage.py makemigrations <앱이름>   // 마이그레이션 파일 생성
	manage.py migrate <앱이름> 		 // 마이그레이션 적용
	manage.py collectstatic 		    //static 파일들을 settings.STATIC_ROOT 경로로 모음
    manage.py --help 				   // 지원하는 명령어 목록
    ```
2. dajngo_rest_tutorial/setting.py

	설치된 APP, MIDDLEWARE, TEMPLATES, WSGI_APPLICATION, DATABASES 등 해당 프로젝트에 대한 설정파일이다.

3. dajngo_rest_tutorial/urls.py

	프로젝트에서 사용하는 url들을 정의하는 부분으로 다음과 같은 규칙을 통해 정의 한다

    ^ 문자열이 시작할 때
	$ 문자열이 끝날 때
	\d 숫자
	\+ 바로 앞에 나오는 항목이 계속 나올 때
	() 패턴의 부분을 저장할 때

4. dajngo_rest_tutorial/wsgi.py

###Database 연동
Django 프로젝트는 기본적으로 sqlite3를 제공한다. 해당 DBMS는 사용가능 하지만 PostgreSQL을 사용하기 위해서는 django\django_rest_tutorial\setting.py파일에서 해당 부분을 변경해야한다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_dev',
        'USER': 'wellstone',
        'PASSWORD': 'dblab321',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

해당 명령을 통해 Django에서 기본적으로 사용하는 테이블 생성

	manage.py makemigrations   // 마이그레이션 파일 생성
	manage.py migrate 		 // 마이그레이션 적용

### super user 생성
```bash
    manage.py createsuperuser
    Username (leave blank to use 'hsoh'): admin
    Email address: wisoft@hanbat.ac.kr
    Password:
    Password (again):
    Superuser created successfully.
```

해당 계정을 생성하면 ```http://localhost:8000/admin/```를 통해 해당 프로젝트 관리를 위한 페이지 접근 가능

### Django REST Framework 사용하기
해당 프로젝트에 Django REST Framework를 사용하는 APP를 생성한다.

```bash
(djangovenv) G:\PyCharm\django\django_rest_tutorial $ >manage.py startapp core
```
dajngo_rest_tutorial/setting.py에 Django REST Framework를 등록한다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```

#### Model 생성
여기서 우리는 대학에 다니는 학생들을 모델링하고 싶다. 먼저 엔티티 클래스와 그 속성을 정의 한다. 학생과 학교의 관계는 1:N 관계로 설정한다.
django\django_rest_tutorial\core\models.py파일을 다음과 같이 수정한다. 
```python
from django.db import models

class University(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
```
dajngo_rest_tutorial/setting.py에 core app를 등록한다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]
```
다음 명령을 통해 DB에 적용한다.
```bash
manage.py makemigrations core
manage.py migrate core
```

적용한 내용을 확인하기 위해 django\django_rest_tutorial\core\admin.py에 등록하면 admin 페이지에서 확인이 가능하다
```python
from django.contrib import admin
from .models import Student, University

admin.site.register(University)
admin.site.register(Student)
```

#### Serializers 생성
HTTP 기반 상호 작용을 수행하기 위해 Django 모델 (파이썬 객체)를 json 문자열로 또는 그 반대로 변환하는 규칙을 정의해야한다. 이것은 직렬화/역직렬화 작업이라고 한다. django\django_rest_tutorial\core\serializers.py 파일에 모델 기반의 시리얼 라이저를 정의한다.

```python
from rest_framework import serializers
from .models import University, Student

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

```

#### View 생성
Django는 전통적인 MVC(model, view, controller) 패턴과 다르게 MVT(model, view, template)패턴을 사용한다. 따라서 Django에서 말하는 View는 MVC에서 ㅊontroller에 해당하는 기능을 하고 template view의 역할을 한다. 따라서 controller에 해당하는 작업을 하는 코드는 django\django_rest_tutorial\core\view.py에 작성한다.
```python
from django.shortcuts import render
from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

```
viewsets는 일련의 뷰 (전통적인 MVC 용어로 컨트롤러)이다. ModelViewSet 코드를 살펴보면 자동으로 많은 기능이 추가되었음을 알 수 있다. 시스템 (및 데이터베이스)에서 오브젝트를 작성,보기, 편집 및 삭제할 수 있다. http를 사용하여 설정 한 전체 CRUD수행 한다.

#### Urls 추가
프로젝트에 있는 urls에 다음과 같이 /api/를 등록하면 core.urls로 이동하여 다음 라우팅을 진행한다.
django\django_rest_tutorial\urls.py
```python 
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('core.urls', namespace='core')),
]

```

/api 이후url은 core APP에 urls에서 라우팅한다.
django\django_rest_tutorial\core\urls.py
```python 
from django.conf.urls import url, include
from rest_framework import routers
from core.views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls

```

### Django_rest_swagger 사용하기
django용 swagger 모듈를 설치한다.
```bash
(djangovenv) G:\PyCharm\django\django_rest_tutorial $ >pip install django-rest-swagger
```
다음 api/docs로 설정하기위해 django\django_rest_tutorial\core\urls.py에 다음과 같이 추가 한다.
```python 
from django.conf.urls import url, include
from rest_framework import routers
from core.views import StudentViewSet, UniversityViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    url(r'^docs/', get_swagger_view(title='Pastebin API')),
]

urlpatterns += router.urls
```

#### 마무리
```bash
(djangovenv) G:\PyCharm\django\django_rest_tutorial $ >manage.py runserver
```
다음 명령을 통해 실행하면 간단하 서버가 완성 됬다.

### Contributors

- 박현주[(phj@hanbat.ac.kr)](phj@hanbat.ac.kr)
- 한밭대학교 무선통신소프트웨어 연구실 NRF-IoT-Platform 연구팀


<br/>
Hanbat National University Wisoft Laboratory