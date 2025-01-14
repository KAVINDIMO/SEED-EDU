from django.urls import path,include
from . import views
from main.views import GoogleLogin

urlpatterns=[
path("",views.home,name="home"),
path("game/",views.game,name="game"),
path("home/",views.home,name="home"),
path("news/",views.news,name="news"),
path("edit/",views.edit,name="profedit"),
path("view/",views.view,name="profview"),
path("books-list/",views.Abooklist,name="books-api"),
path("news-list/",views.Anewslist,name="news-api"),
path("users-list/",views.Auserslist,name="users-api"),
path("acollege-list/",views.Aallcollegelist,name="colleges-api"),
path("tcollege-list/",views.Atopcollegelist,name="colleges-api"),
path("dcollege-list/",views.Adegreecollegelist,name="colleges-api"),
path("scollege-list/",views.Astatecollegelist,name="colleges-api"),
path("ccollege-list/",views.Acitycollegelist,name="colleges-api"),
path("coursecollege-list/",views.Acoursecollegelist,name="colleges-api"),
path("paper-list/",views.Apaperlist,name="papers-api"),
path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
path("artscourse-list/",views.Aartscourselist,name="arts-api"),
path("sciencecourse-list/",views.Asciencecourselist,name="science-api"),
path("engineeringcourse-list/",views.Aengineeringcourselist,name="engineering-api"),
path("commercecourse-list/",views.Acommercecourselist,name="commerce-api"),
path("professionalcourse-list/",views.Aprofessionalcourselist,name="professional-api"),
path("dates-list/",views.Adateslist,name="dates-api"),
path("qptypes-list/",views.Aquestionbanktypeslist,name="qpbanktypes-api"),
path("qps-list/<str:key>/",views.Aquestionbanklist,name="qpbank-api"),
path("rnotes-list/",views.Arnoteslist,name="rnotes-api"),
path("rnotes-list/<str:key>/",views.Anotelist,name="note-api"),
path("tips-list/",views.Atipslist,name="tips-api"),
path("ocourses-list/",views.Aocourseslist,name="ocourses-api"),
path("videos-list/",views.Avideolist,name="videos-api"),
path("sbooks-list/<str:key>/",views.Abookstandardlist,name="standardbook-api"),
path("quiz-list/<str:key>/<str:reqid>/",views.Aquizlist,name="quiz-api"),
path("attquiz-list/<str:key>/",views.Aattquizlist,name="attquiz-api"),
path("quizans-list/<str:key>/",views.Aquizanslist,name="quizans-api"),
path("quizansatt-list/<str:tid>/<str:key>/",views.Aquizansattlist,name="quizans-api"),
path("quizresult-list/<str:sid>/<str:mil>/<str:std>/<str:tid>/<str:pnt>/",views.Aquizresultlist,name="quizresult-api"),
path("quizrresult-list/<str:mil>/",views.Aqresultlist,name="quizresult-api"),
path("mock-list/<str:std>/<str:mil>/",views.Amocklist,name="mock-api"),
path("attmock-list/<str:std>/<str:mil>/",views.Aattmocknamelist,name="attmock-api"),
path("viewmockans-list/<str:tid>/",views.Aattmocklist,name="attmock-api"),
path("mockqp-list/<str:tid>/",views.Amockqplist,name="mockqp-api"),
path("mocktempo-list/<str:nme>/<str:mil>/",views.Amtempolist,name="temporesult-api"),
path("mockrresult-list/<str:mil>/",views.Amresultlist,name="mockresult-api"),
path("sbook-list/<str:grd>/",views.Sbooklist,name="sbook-api"),
path("qptypes-list/<str:grd>/",views.Squesbank,name="squesbank-api"),
path("bpapers-list/<str:uid>/",views.Sbpapers,name="sbpapers-api"),
path("revnotes-list/<str:grd>/",views.Srevnotes,name="srevnotes-api"),
path("addbook-list/",views.Abooklist,name="addbooks-api"),
path("tbook-list/<str:adb>/",views.Atbooklist,name="teacherviewbooks-api"),
path("tdelbook-list/<str:adb>/<str:bid>/",views.Atdelbooklist,name="delTbooks-api")
]