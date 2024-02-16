var sectionArray = [1, 2, 3, 4, 5]

$.each(sectionArray, function (index, value) {
  $(document).scroll(function () {
    var offsetSection = $("#" + "section" + value).offset().top
    var docScroll = $(document).scrollTop()
    var docScroll1 = docScroll + 1

    if (docScroll1 >= offsetSection) {
      $(".navbar-nav .nav-link").removeClass("active")
      $(".navbar-nav .nav-link:link").addClass("inactive")
      $(".navbar-nav .nav-item .nav-link").eq(index).addClass("active")
      $(".navbar-nav .nav-item .nav-link").eq(index).removeClass("inactive")
    }
  })

  $(".click-scroll")
    .eq(index)
    .click(function (e) {
      var offsetClick = $("#" + "section" + value).offset().top
      e.preventDefault()
      $("html, body").animate(
        {
          scrollTop: offsetClick,
        },
        300
      )
    })
})

// // postcss.config.js
// module.exports = {
//   plugins: {
//     tailwindcss: {},
//     autoprefixer: {},
//   },
// }

// //Variables
// const btn = document.querySelector(".mobile-menu-button")
// const menu = document.querySelector(".mobile-menu")

// // Event listeners
// btn.addEventListener("click", () => {
//   menu.classList.toggle("hidden")
// })
