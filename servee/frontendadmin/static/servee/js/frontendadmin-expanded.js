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

                    // I changed the django "module" table into a vertical form display using some
                    // CSS trickery. Here, I take the labels from the table display and insert
                    // them into the right places with CSS. Since pseudo-elements can't be applied
                    // inline, this is sort of complicated. The CSS is taking the text from the
                    // data-content attribute, which I'm adding below. --KK

                    var head1 = $("#servee_container .module th:nth-of-type(1)").text();
                    var head2 = $("#servee_container .module th:nth-of-type(2)").text();
                    var head3 = $("#servee_container .module th:nth-of-type(3)").text();
                    var head4 = $("#servee_container .module th:nth-of-type(4)").text();
                    var head5 = $("#servee_container .module th:nth-of-type(5)").text();
                    var head6 = $("#servee_container .module th:nth-of-type(6)").text();
                    var head7 = $("#servee_container .module th:nth-of-type(7)").text();
                    var head8 = $("#servee_container .module th:nth-of-type(8)").text();
                    var head9 = $("#servee_container .module th:nth-of-type(9)").text();
                    var head10 = $("#servee_container .module th:nth-of-type(10)").text();

                    $("#servee_container .module td:nth-of-type(2)").attr('data-content', head1 );
                    $("#servee_container .module td:nth-of-type(3)").attr('data-content', head2 );
                    $("#servee_container .module td:nth-of-type(4)").attr('data-content', head3 );
                    $("#servee_container .module td:nth-of-type(5)").attr('data-content', head4 );
                    $("#servee_container .module td:nth-of-type(6)").attr('data-content', head5 );
                    $("#servee_container .module td:nth-of-type(7)").attr('data-content', head6 );
                    $("#servee_container .module td:nth-of-type(8)").attr('data-content', head7 );
                    $("#servee_container .module td:nth-of-type(9)").attr('data-content', head8 );
                    $("#servee_container .module td:nth-of-type(10)").attr('data-content', head9 );
                    $("#servee_container .module td:nth-of-type(11)").attr('data-content', head10 );
                    $("#servee_container .module thead").hide();



                   e.preventDefault();
                   return false;
                });
            }
        });

        e.preventDefault();
        return false;
    });
});
