$(document).ready(function(){function t(t){var e="div, article, section, aside, header, footer, body";return"undefined"!=typeof servee&&"undefined"!=typeof servee.selector?$(servee.selector):(console.log(t.parents(e).eq(0)),t.parents(e).eq(0))}$("a.frontendadmin_edit:not(.modal)").hover(function(){var e=$(this),n;n=t(e),n.addClass("pre-edit")},function(){var e=$(this),n;n=t(e),n.removeClass("pre-edit")}),$("a.frontendadmin_delete:not(.modal)").hover(function(){var e=$(this),n;n=t(e),n.addClass("pre-delete")},function(){var e=$(this),n;n=t(e),n.removeClass("pre-delete")}),$("a.frontendadmin_add").on("click",function(e){var n=$(this),a;return a=t(n),$.ajax({url:this.href,success:function(t,e){a.html(t)}}),e.preventDefault(),!1}),$("a.frontendadmin_list").on("click",function(e){var n=$(this),a;return a=t(n),$.ajax({url:this.href,success:function(t,e){a.html(t)}}),e.preventDefault(),!1}),$("a.frontendadmin_edit").on("click",function(e){var n=$(this),a;return a=t(n),console.log(a),a.css("outline",""),$.ajax({url:this.href,success:function(t,n){function o(){$("#servee_container .module table").each(function(){var t=$(this).find("th:nth-of-type(1)").text(),n=$(this).find("th:nth-of-type(2)").text(),a=$(this).find("th:nth-of-type(3)").text(),o=$(this).find("th:nth-of-type(4)").text(),i=$(this).find("th:nth-of-type(5)").text(),r=$(this).find("th:nth-of-type(6)").text(),d=$(this).find("th:nth-of-type(7)").text(),h=$(this).find("th:nth-of-type(8)").text(),f=$(this).find("th:nth-of-type(9)").text(),s=$(this).find("th:nth-of-type(10)").text();return $("td:nth-of-type(2)").attr("data-content",t),$("td:nth-of-type(3)").attr("data-content",n),$("td:nth-of-type(4)").attr("data-content",a),$("td:nth-of-type(5)").attr("data-content",o),$("td:nth-of-type(6)").attr("data-content",i),$("td:nth-of-type(7)").attr("data-content",r),$("td:nth-of-type(8)").attr("data-content",d),$("td:nth-of-type(9)").attr("data-content",h),$("td:nth-of-type(10)").attr("data-content",f),$("td:nth-of-type(11)").attr("data-content",s),$("thead").hide(),e.preventDefault(),!1})}a.html(t),$(".file-upload a").not("[href*='.pdf']").each(function(){var t=$(this).attr("href");t&&$(this).prepend('<img src="'+t+'" style="max-width:180px;max-height:100px;margin-bottom:10px;display:block;">')}),$("#images-group").before("<a href='#' id='gallery_dropdown'>Edit the gallery for this page <span>›</span></a>"),$("#images-group").hide(),$("#gallery_dropdown").on("click",function(t){$("#images-group").toggle(),o()}),o()}}),e.preventDefault(),!1})});