var updateBtns = document.getElementsByClassName('update-cart')
console.log(updateBtns.length)
for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'action:', action)

        console.log('User:', user)
        if(user === 'AnonymousUser'){
            console.log('not logged in')
        }else{
            /*console.log('User is logged in, sending data..')*/
            updateUserOrder(productId, action)
        }
    })
    }

    function updateUserOrder(productId,action){
        console.log('User is authenticated, sending data..')

        var url = $("#Url").attr("data-url");
        console.log("trying to post to url: " + url)
        console.log("csrf token: " + csrftoken)
        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFtoken':csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'action':action, 'csrfmiddlewaretoken': csrftoken})
        })
        .then((response) =>{
            return response.json();
        })
        .then((data) =>{
            console.log('data', data)
            location.reload()
        })
    }


console.log("hello")