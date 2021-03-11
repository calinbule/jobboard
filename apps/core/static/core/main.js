/*var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;*/

tinymce.init({
    selector:'textarea',
    plugins: 'print preview paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons',
    menubar: 'edit view insert format tools table',
    toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | fullscreen  preview | insertfile image media link anchor codesample | ltr rtl',
    toolbar_sticky: true,
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false, /* set this to true ??? */
    autosave_retention: '2m',
    image_advtab: true,
    height: 600,
    /*image_caption: true,*/
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    noneditable_noneditable_class: 'mceNonEditable', /* do we really need this ??? */
    toolbar_mode: 'sliding', /* Possible Values: 'floating', 'sliding', 'scrolling', or 'wrap' */
    contextmenu: 'link image imagetools table',
    /* skin: useDarkMode ? 'oxide-dark' : 'oxide',
    content_css: useDarkMode ? 'dark' : 'default', */
    skin:'oxide',
    content_css: 'default',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',
    importcss_append: true,
});