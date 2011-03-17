$(document).ready(function(){
	$("a.frontendadmin_edit").hover(
	    function(){$(this).parent().css("outline", "4px solid #eeeeee");},
	    function(){$(this).parent().css("outline", "");}
	);
	$("a.frontendadmin_delete").hover(
	    function(){$(this).parent().css("outline", "4px solid #8C1717");},
	    function(){$(this).parent().css("outline", "");}
	);

	$("a.frontendadmin_add").click(function(e){
		var $base, $par = $(this).parent();
	    $par.css("outline", "");
	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            $par.html(data);
	        }
	    });
	    e.preventDefault();
	    return false;
	});


	$("a.frontendadmin_edit").click(function(e){
		var $base, $par = $(this).parent();
	    $par.css("outline", "");
	    $.ajax({
	        url: this.href,
	        success: function(data, text){
	            $par.html(data);
	        }
	    });
	    e.preventDefault();
	    return false;
	});

	/**************************
	 * Insert Tools 
	 **************************/
	// Clicking of 1st tier, building of 2nd tier
	$(".srv_mediaList li a").live("click", function(e){
		var $link = $(this);
	
	
		//@@ TODO currentInsert is a global object.  This is lame,
		//servee should have only one global object.
		currentInsert = $link.attr("data-slug");
	
		$.ajax({
            url: $link.attr("href"),
            success: function(data, text){
                console.log(data);
                $(".srv_filePane").remove();
                $(".srv_insertOptions").remove();
                $(".srv_mediaList").after(
                    "<div id='srv_"+currentInsert+"_filePane' class='srv_filePane'>"
                    + data
                    + "</div>"
                );
                //Once the dom is rebuilt, slide it in.
                srv_show_adminBox("srv_insertMedia");
            }
        });
		e.preventDefault();
		return false;
	});

	// Clicking of 2nd tier, building of 3rd tier
	$(".srv_filePane li a").live("click", function(e){
		var $link = $(this);
		$.ajax({
            url: $link.attr("href"),
            success: function(data, text){
                console.log(data);
                $(".srv_insertOptions").remove();
                $(".srv_filePane").after(
                    "<div id='srv_"+ currentInsert +"_insertOptions' class='srv_insertOptions'>"
                    + data
                    + "</div>"
                );
                //Once the dom is rebuilt, slide it in.
                srv_show_adminBox("srv_insertMedia");
            }
        });
		e.preventDefault();
		return false;
	});

});