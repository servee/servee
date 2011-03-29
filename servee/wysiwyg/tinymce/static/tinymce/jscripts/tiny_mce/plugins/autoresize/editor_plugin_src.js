(function() {

    /**
     * Auto Resize
     * 
     * This plugin automatically resizes the content area to fit its content height.
     * It will retain a minimum height, which is the height of the content area when
     * it's initialized.
     * 
     * Tested in: IE6, IE7, IE8 as IE7, IE8 as IE8, Safari 3, Firefox 3, Opera 9, Chrome 1
     * 
     * Known issues: None
     * 
     * Change log:
     * - 1.2: Changed hiding all scrollbars to just hiding the vertical one, so you can still
     *        have a horizontal scrollbar for wide content. Also added an onload handler to the
     *        iframe, so that the area resizes after all of the iframe's content has loaded.
     * - 1.1: Added throbber and disabled editor until we're pretty sure that all CSS has loaded.
     *        This should fix an issue where the content area would not resize properly on load
     *        for people on slower connections.
     * - 1.0: Initial release
     * 
     * Not tested with Advanced Theme "theme_advanced_resizing_min_height" and 
     * "theme_advanced_resizing_max_height" options.
     *
     * @author Springload
     * @version 1.1
     * @requires TinyMCE 3+
     */
    tinymce.create('tinymce.plugins.AutoResizePlugin', {
        /**
         * Initializes the plugin, this will be executed after the plugin has been created.
         * This call is done before the editor instance has finished it's initialization so use the onInit event
         * of the editor instance to intercept that event.
         *
         * @param {tinymce.Editor} ed Editor instance that the plugin is initialized in.
         * @param {string} url Absolute URL to where the plugin is located.
         */
        init : function(ed, url) {                       
        
            // Create namespace for variables on the editor instance
            tinymce.createNS('springload',ed);
            
            // Backup TinyMCE default focus function, to prevent jumping in IE
            ed.springload.defaultFocus = ed.focus;
            ed.focus = function(){}
            
            // Define minimum height in the namespace
            ed.springload.autoresize_min_height = ed.getElement().offsetHeight;
            
            // Things to do before the editor is ready
            ed.onPreInit.add(function(ed) {
                
                // Get content element, store it in the namespace
                ed.springload.content_container = ed.getContentAreaContainer().firstChild;
                
                // Add onload listener to IFRAME
                if(ed.springload.content_container.tagName == 'IFRAME'){
                    
                    tinymce.dom.Event.add(ed.springload.content_container, 'load', function(e) {
                        tinymce.EditorManager.get(ed.id).execCommand('mceAutoResize');
                    });
                    
                }
                
            });
            
            // Things to do when the editor is ready
            ed.onInit.add(function(ed, l) {
                
                // Show throbber until content area is resized properly
                ed.setProgressState(true);
                ed.springload.throbbing = true;
                
                // Hide scrollbars
                ed.getBody().style.overflowY = "hidden";
                
            });
            
            // Add appropriate listeners for resizing content area
            ed.onChange.add(function(ed, l) {
                ed.execCommand('mceAutoResize');
            });
            ed.onSetContent.add(function(ed, l) {
                ed.execCommand('mceAutoResize');
            });
            ed.onPaste.add(function(ed, l) {
                ed.execCommand('mceAutoResize');
            });
            ed.onKeyUp.add(function(ed, l) {
                ed.execCommand('mceAutoResize');
            });
            ed.onPostRender.add(function(ed, l) {
                ed.execCommand('mceAutoResize');
            });       
            ed.onLoadContent.add(function(ed, l) {
                ed.execCommand('mceAutoResize');
                // Because the content area resizes when its content CSS loads,
                // and we can't easily add a listener to its onload event,
                // we'll just trigger a resize after a short loading period
                setTimeout("tinymce.EditorManager.get('" + ed.id + "').execCommand('mceAutoResizeTimeout');",1250);
            });
            
            // Interval resize trigger function
            ed.addCommand('mceAutoResizeTimeout', function() {
                // Resize
                this.execCommand('mceAutoResize');
                // Disable throbber
                this.setProgressState(false);
                this.springload.throbbing = false;
                // Restore TinyMCE default focus function
                if(typeof(this.springload.defaultFocus) == "function"){
                    this.focus = this.springload.defaultFocus;
                    this.springload.defaultFocus = false;
                }
            });
            
            // Register the command so that it can be invoked by using tinyMCE.activeEditor.execCommand('mceExample');
            ed.addCommand('mceAutoResize', function() {
                // Variables
                var d = this.getDoc(), b = d.body, de = d.documentElement, DOM=tinymce.DOM, resizeHeight=this.springload.autoresize_min_height;
                
                // Get height differently depending on the browser used
                (tinymce.isIE) ? myHeight = b.scrollHeight : myHeight = de.offsetHeight;
                
                // Don't make it smaller than the minimum height
                if(myHeight > this.springload.autoresize_min_height){
                    resizeHeight = myHeight;   
                }                                
                
                // Resize content element
                DOM.setStyle(this.springload.content_container, 'height', resizeHeight + 'px');
                
                // if we're throbbing, we'll re-throb to match the new size
                if(this.springload.throbbing){
                    this.setProgressState(false);
                    this.setProgressState(true);
                }
                
            });
                 

        },
        
        /**
         * Returns information about the plugin as a name/value array.
         * The current keys are longname, author, authorurl, infourl and version.
         *
         * @return {Object} Name/value array containing information about the plugin.
         */
        getInfo : function() {
            return {
                longname : 'Auto Resize',
                author : 'Springload',
                authorurl : 'http://www.springload.co.nz',
                infourl : 'http://wiki.moxiecode.com/index.php/TinyMCE:Plugins',
                version : "1.2"
            };
        }

    });
   
    // Register plugin
    tinymce.PluginManager.add('autoresize', tinymce.plugins.AutoResizePlugin);
})();