(function ($) {
    "use strict";
    var initColorPicker = function (selector) {
        $(selector).ColorPicker({
            onSubmit: function(hsb, hex, rgb, el, parent) {
                $(el).val('#' + hex);
                $(el).ColorPickerHide();
            },
            onBeforeShow: function () {
                $(this).ColorPickerSetColor(this.value);
            }
        }).bind('keyup', function(){
            $(this).ColorPickerSetColor(this.value.replace('#', ''));
        });
    };

    $(document).on('ready', function() {
        initColorPicker($('input[type=colorpicker]'));
    });

    $(document).on('click', '.add-row a, .grp-add-handler', function() {
        var $newSlide = $(this).parent().siblings('.dynamic-slides:not(.empty-form):last');
        var $colorpicker = $newSlide.find('input[type=colorpicker]');
        initColorPicker($colorpicker);
    });
}(jQuery || django.jQuery));
