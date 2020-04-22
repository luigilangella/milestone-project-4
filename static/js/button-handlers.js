$(document).ready(function() {
    $(".likebutton").submit(function(event) {
        event.preventDefault(); //prevent default action 
        var post_url = $(this).attr("action"); //get form action url
        var form_data = $(this).serialize(); //Encode form elements for submission

        $.post(post_url, form_data, function(response) {
            $('#likes-' + response.id).text(response.likes);
            $('#dislikes-' + response.id).text(response.dislikes);
        });
    });

    $(".dislikebutton").submit(function(event) {
        event.stopImmediatePropagation();
        event.preventDefault(); //prevent default action 
        var post_url = $(this).attr("action"); //get form action url
        var form_data = $(this).serialize(); //Encode form elements for submission

        $.post(post_url, form_data, function(response) {
            $('#likes-' + response.id).text(response.likes);
            $('#dislikes-' + response.id).text(response.dislikes);
        });
    });
});