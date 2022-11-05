const model: Model = new Model();
const view: View = new View();

$("#search-button").on("click", function(){
    const ingredientName: string = <string> $("#content").val()
    const glutenIsClikced: boolean = $("#gluten-checkbox").is(":checked")
    const diaryIsClikced: boolean = $("#dairy-checkbox").is(":checked")
    model.getRecipesFromServer(ingredientName, glutenIsClikced, diaryIsClikced).then((result:any) => {
        view.render(result)             
    })        

})

