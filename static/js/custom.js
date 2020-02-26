$(document).ready(function () {

    /* initialization */
    $('.slider').slider();
    $('select').formSelect();
    $('.modal').modal();
    $(".dropdown-trigger").dropdown();
    $(".mobilie-menu").dropdown();
    $('.sidenav').sidenav();
});

    /* Dynamically add new input field to ingredients form*/
    $(".add-input-field").on("click", function () {
        $('<input type="text" class="validate" name="ingredients" placeholder="Add next ingredient" required >').insertBefore(".add-input-field");
    });

    /* Removes last input element from ingredients form*/
    $(".delete-last-field").on("click", function () {
        $("#items input:last").remove();
    });

    /* Dynamically add new input field to steps form */
    $(".add-step").on("click", function () {
        $('<textarea name="method" class="materialize-textarea" placeholder="Add next step" required ></textarea>').insertBefore(".add-step");
    });
 
    /* Removes last input element from steps form */
    $(".delete-last-step").on("click", function () {
        $("#steps textarea:last").remove();
    });



/* page printing function */
function printRecipe() {
    window.print();
}