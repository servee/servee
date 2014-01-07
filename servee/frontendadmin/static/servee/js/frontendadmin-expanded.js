$(document).ready(function(){

    function set_parent($link){
        var REPLACE_BLOCKS = "div, article, section, aside, header, footer, body";

        if ((typeof(servee) != "undefined") && (typeof(servee.selector) != "undefined")){
            return $(servee.selector);
        }
        console.log($link.parents(REPLACE_BLOCKS).eq(0));
        return $link.parents(REPLACE_BLOCKS).eq(0);
    }

    /* Frontendadmin buttons add, edit, delete */
    $("a.frontendadmin_edit:not(.modal)").hover(
        function(){
            var $link = $(this), $par;
            $par = set_parent($link);
            $par.addClass("pre-edit");
        },
        function(){
            var $link = $(this), $par;
            $par = set_parent($link);
            $par.removeClass("pre-edit");
        }
    );
    $("a.frontendadmin_delete:not(.modal)").hover(
        function(){
            var $link = $(this), $par;
            $par = set_parent($link);
            $par.addClass("pre-delete");
        },
        function(){
            var $link = $(this), $par;
            $par = set_parent($link);
            $par.removeClass("pre-delete");
        }
    );

    $("a.frontendadmin_add").on("click", function(e){
        var $link = $(this), $par;
        $par = set_parent($link);
        $.ajax({
            url: this.href,
            success: function(data, text){
                $par.html(data);
            }
        });
        e.preventDefault();
        return false;
    });

    $("a.frontendadmin_list").on("click", function(e){
        var $link = $(this), $par;
        $par = set_parent($link);
        $.ajax({
            url: this.href,
            success: function(data, text){
                $par.html(data);
            }
        });

        e.preventDefault();
        return false;
    });

    $("a.frontendadmin_edit").on("click", function(e){
        var $link = $(this), $par;
        $par = set_parent($link);
        console.log($par);
        $par.css("outline", "");
        $.ajax({
            url: this.href,
            success: function(data, text){
                $par.html(data);
                $('.file-upload').each(function(){
                    var thumbURL = $(this).children('a').attr('href');
                    if (thumbURL){
                        $(this).prepend('<img src="' + thumbURL + '" style="max-width:180px;max-height:100px;margin-bottom:10px;display:block;">');
                    }
                });
                // hide galleries, because they make the form crazy long
                $('#images-group').before("<a href='#' id='gallery_dropdown'>Edit the gallery for this page <span>›</span></a>");
                $('#images-group').hide();
                $('#gallery_dropdown').on("click", function(e){
                   $('#images-group').toggle();
                   e.preventDefault();
                    return false;
                });
            }
        });

        e.preventDefault();
        return false;
    });


});
