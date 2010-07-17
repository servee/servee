/*
 * Superfish v1.3.4 - jQuery menu widget
 *
 * Copyright (c) 2007 Joel Birch
 *
 * Dual licensed under the MIT and GPL licenses:
 * 	http://www.opensource.org/licenses/mit-license.php
 * 	http://www.gnu.org/licenses/gpl.html
 */



(function($){
	$.fn.superfish = function(o){
		var $sf = this,
			defaults = {
			hoverClass	: 'sfHover',
			pathClass	: 'overideThisToUse',
			delay		: 800,
			animation	: {opacity:'show'},
			speed		: 'normal',
			onshow		: function(){} // in your function, 'this' is the revealed ul
		},
			over = function(){
				clearTimeout(this.sfTimer);
				$(this)
				.showSuperfishUl(o)
				.siblings()
				.hideSuperfishUl(o);
			},
			out = function(){
				var $$ = $(this);
				if ( !$$.is('.'+o.bcClass) ) {
					this.sfTimer=setTimeout(function(){
						$$.hideSuperfishUl(o);
						var sf = $$.parents('ul.superfish:first')[0];
						if (!$('.'+o.hoverClass,sf).length) {
							over.call(sf.o.$currents.hideSuperfishUl(o));
						}
					},o.delay);
				}		
			};
		$.fn.extend({
			hideSuperfishUl : function(o){
				$('li.'+o.hoverClass,this)
				.andSelf()
					.removeClass(o.hoverClass)
					.find('>ul')
						.hide()
						.css('visibility','hidden');
				return this;
			},
			showSuperfishUl : function(o){
				return this
					.addClass(o.hoverClass)
					.find('>ul:hidden')
						.css('visibility','visible')
						.animate(o.animation,o.speed,function(){
							o.onshow.call(this);
						})
					.end();
			},
			applySuperfishHovers : function(){
				return this[($.fn.hoverIntent) ? 'hoverIntent' : 'hover'](over,out);
			}
		});
		
		return this
		.addClass('superfish')
		.each(function(){
			o = $.extend({bcClass:'sfbreadcrumb'},defaults,o);
			o = $.extend(o,{$currents:$('li.'+o.pathClass,this)});
			this.o = o;
			
			if (o.$currents.length) {
				o.$currents.each(function(){
					$(this)
					.addClass(o.hoverClass+' '+o.bcClass)
					.filter(':has(ul)')
						.removeClass(o.pathClass);
				});
			}
			
			var $sfHovAr=$('li:has(ul)',this)
				.applySuperfishHovers(over,out)
				.not('.'+o.bcClass)
					.hideSuperfishUl(o)
				.end();
			
			$('a',this).each(function(){
				var $a = $(this), $li = $a.parents('li');
				$a.focus(function(){
					over.call($li);
					return false;
				}).blur(function(){
					$li.removeClass(o.hoverClass);
				});
			});
		});
	};
	$(window).unload(function(){
		$('ul.superfish').each(function(){
			$('li:has(ul)',this).unbind('mouseover').unbind('mouseout');
			this.o = this.o.$currents = null; // clean up
		});
	});
})(jQuery);