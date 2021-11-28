class CommonJs {
    getSuccessToastOptions() {
        return {
            theme: "bubble", 
            position: "top-center", 
            duration : 2000
        }
    }
}

export let $CommonJs = new CommonJs();