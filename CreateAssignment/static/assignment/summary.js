$('#add_sub_question').click(function () {
    $.ajax(
        {
            type: "GET",
            url: "./addsubquestion",
            success: function (data) {
                console.log(data, data["status"])
                if (data["status"] == true) {

                    let leng = document.getElementsByClassName("subquestion").length
                    let ids = document.getElementsByName("sq_id");
                    let text = document.getElementsByName("text");
                    let answer = document.getElementsByName("answer");
                    let explanation = document.getElementsByName("explanation");
                    let score = document.getElementsByName("score");
                    let arr = [];
                    for (let i = 0; i < leng; i++) {
                        ids[i].innerText = ids[i].value;
                        text[i].innerText = text[i].value;
                        answer[i].innerText = answer[i].value;
                        explanation[i].innerText = explanation[i].value;
                        arr.push(score[i].value);
                    }



                    already = document.getElementById("subquestions").innerHTML;
                    addone = ` 
                    <hr>
                    <div class="subquestion">
                        <input type="hidden" name = "sq_id" value= "${data.id}">
                        <textarea name="text"  cols="30" rows="10" placeholder = 'Your question here' ></textarea>
                        <textarea name="answer"  cols="30" rows="10" placeholder = 'Correct Answer here'></textarea>
                        <textarea name="explanation"  cols="30" rows="10" placeholder = 'explanation'></textarea>
                        <input type= "number" name="score" value="1" placeholder = 'score' >
                        <br>
                    </div>`;

                    document.getElementById("subquestions").innerHTML = already + addone
                    for (let i = 0; i < leng; i++) {
                        score[i].value = arr[i];
                    }

                }
            }
        })
});


// function savedata(token){
$(".submitb").click(function () {
    $.ajax(
        {
            type: "POST",
            url: "./savequestion",
            data: {
                'data': savedata(),
                'csrfmiddlewaretoken': token
            },
            success: function (data) {
                if (data["status"]) {
                    console.log('updated');
                } else {
                    console.log("couldn't update");
                }
            }
        })

});
// }

function savedata() {
    console.log(token)
    subquestions = []
    let leng = document.getElementsByClassName("subquestion").length
    let ids = document.getElementsByName("sq_id");
    let text = document.getElementsByName("text");
    let answer = document.getElementsByName("answer");
    let explanation = document.getElementsByName("explanation");
    let score = document.getElementsByName("score");

    for (let i = 0; i < leng; i++) {
        temp = {};
        // id = 
        temp["id"] = ids[i].value;
        temp["text"] = text[i].value;
        temp["answer"] = answer[i].value;
        temp["explanation"] = explanation[i].value;
        temp["score"] = score[i].value;
        subquestions.push(temp);
    }

    output = {
        "subquestions": subquestions,
        "question": document.getElementsByName("question")[0].value,
        // "csrfmiddlewaretoken" : document.getElementsByName("csrfmiddlewaretoken")[0].value
    };
    console.log("from here: ")
    console.log(JSON.stringify(output))
    return JSON.stringify(output);
}