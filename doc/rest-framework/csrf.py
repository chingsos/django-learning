#coding:utf-8

"""
前端js开发时，充分利用 restframework提供的static资源 ,
直接引入 rest_framework/js/csrf.js 即可自动完成 csrf-token的获取 ( server端要开启 crsfMiddleWare)

restframework 自带了js包括:  booststrap,ajax-form ,jquery,prettify(格式化代码)

	deafult.js
		prettyPrint() 高亮输出json代码

	<link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/bootstrap.min.css" %}"/>
    <link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/bootstrap-tweaks.css" %}"/>
	<link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/prettify.css" %}"/>
    <link rel="stylesheet" type="text/css" href="{% static "rest_framework/css/default.css" %}"/>

	{% block script %}
		<script src="{% static "rest_framework/js/jquery-1.11.3.min.js" %}"></script>
		<script src="{% static "rest_framework/js/ajax-form.js" %}"></script>
		<script src="{% static "rest_framework/js/csrf.js" %}"></script>
		<script src="{% static "rest_framework/js/bootstrap.min.js" %}"></script>
		<script src="{% static "rest_framework/js/prettify-min.js" %}"></script>
		<script src="{% static "rest_framework/js/default.js" %}"></script>
		<script>
			$(document).ready(function() {
				$('form').ajaxForm();
			});
		</script>
  	{% endblock %}

"""

"""
中间件 CSrfViewMiddleware 的 response处理时，先判别 request中是否已经携带 CSRF_TOKEN,如果已携带则不做处理，直接返回上级middleware的处理结果，
否则，创建CSRF_TOKEN 并返回response. 
默认cookie：  
	csrftoken=rHbOGZ2m8PdNcToHisdiac8uDcXgLEMp

传递 csrf token : 

	POST 请求中添加 csrfmiddlewaretoken 字段 
或者：
	Header 中 添加 HTTP_X_CSRFTOKEN 字段

"""

"""

easyui 使用注意： 
	通过设置  $.ajaxSetup() ,提交数据时发送X-CSRFToken 头
	提交ajax请求千万不能采用  $.form('submit') ，因为其不会触发 $.ajaxSetup() 


"""

"""

function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');

        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;

    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') || (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
    // or any other URL that isn't scheme relative or absolute i.e relative.
    !(/^(\/\/|http:|https:).*/.test(url));
}

var csrf_cookie_name = 'csrftoken';
var csrftoken = getCookie(csrf_cookie_name);
var csrf_head_name = 'X-CSRFToken';

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            //xhr.setRequestHeader(window.drf.csrfHeaderName, csrftoken);
            xhr.setRequestHeader( csrf_head_name, csrftoken);
        }
    }
});

"""


