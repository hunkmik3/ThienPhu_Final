/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

(function ($) {
  'use strict';

  /* ========================================================================= */
  /*	Page Preloader
  /* ========================================================================= */
  $(window).on('load', function () {
    $('#preloader').fadeOut('slow', function () {
      $(this).remove();
    });
  });


  // navbarDropdown
  if ($(window).width() < 992) {
    $('#navigation .dropdown-toggle').on('click', function () {
      $(this).siblings('.dropdown-menu').animate({
        height: 'toggle'
      }, 300);
    });
  }

  //Hero Slider
  $('.hero-slider').slick({
    autoplay: true,
    infinite: true,
    arrows: true,
    prevArrow: '<button type=\'button\' class=\'prevArrow\'></button>',
    nextArrow: '<button type=\'button\' class=\'nextArrow\'></button>',
    dots: false,
    autoplaySpeed: 7000,
    pauseOnFocus: false,
    pauseOnHover: false
  });
  $('.hero-slider').slickAnimation();

  /* ========================================================================= */
  /*	Portfolio Filtering Hook
  /* =========================================================================  */
  // filter - only initialize if container exists
  setTimeout(function () {
    var containerEl = document.querySelector('.filtr-container');
    var filterizd;
    if (containerEl && containerEl.children.length > 0) {
      try {
        filterizd = $('.filtr-container').filterizr({
          animationDuration: 0.5,
          delay: 0,
          delayMode: 'progressive'
        });
      } catch (e) {
        console.log('Filterizr initialization error:', e);
      }
    }
  }, 500);

  /* ========================================================================= */
  /*	Testimonial Carousel
  /* =========================================================================  */
  //Init the slider
  $('.testimonial-slider').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000
  });


  /* ========================================================================= */
  /*	Clients Slider Carousel
  /* =========================================================================  */
  //Init the slider
  $('.clients-logo-slider').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
    responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false
      }
    }
    ]
  });

  /* ========================================================================= */
  /*	Company Slider Carousel
  /* =========================================================================  */
  $('.company-gallery').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
    responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 667,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        arrows: false
      }
    }
    ]
  });

  /* ========================================================================= */
  /*	Projects Slider Carousel
  /* =========================================================================  */
  $('.projects-slider').slick({
    infinite: true,
    arrows: true,
    prevArrow: '<button type=\'button\' class=\'prevArrow projects-prev\'></button>',
    nextArrow: '<button type=\'button\' class=\'nextArrow projects-next\'></button>',
    dots: true,
    autoplay: true,
    autoplaySpeed: 5000,
    pauseOnHover: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    fade: false,
    cssEase: 'linear'
  });

  /* ========================================================================= */
  /*	On scroll fade/bounce effect
  /* ========================================================================= */
  // Only apply smooth scroll to anchor links on the same page (not external links or links to other pages)
  // Exclude navigation links and links that go to other pages
  var scrollLinks = document.querySelectorAll('a[href^="#"]:not([href="#"]):not(.nav-link):not([href*=".html"])');
  if (scrollLinks.length > 0) {
    try {
      var scroll = new SmoothScroll('a[href^="#"]:not([href="#"]):not(.nav-link):not([href*=".html"])', {
        speed: 500,
        speedAsDuration: true,
        offset: 80,
        updateURL: false,
        popstate: false
      });
    } catch (e) {
      console.log('SmoothScroll initialization error:', e);
    }
  }

  // -----------------------------
  //  Count Up
  // -----------------------------
  function counter() {
    var oTop;
    if ($('.counter').length !== 0) {
      oTop = $('.counter').offset().top - window.innerHeight;
    }
    if ($(window).scrollTop() > oTop) {
      $('.counter').each(function () {
        var $this = $(this),
          countTo = $this.attr('data-count');
        $({
          countNum: $this.text()
        }).animate({
          countNum: countTo
        }, {
          duration: 1000,
          easing: 'swing',
          step: function () {
            $this.text(Math.floor(this.countNum));
          },
          complete: function () {
            $this.text(this.countNum);
          }
        });
      });
    }
  }
  // -----------------------------
  //  On Scroll
  // -----------------------------
  $(window).scroll(function () {
    counter();

    // var scroll = $(window).scrollTop();
    // if (scroll > 50) {
    //   $('.navigation').addClass('sticky-header');
    // } else {
    //   $('.navigation').removeClass('sticky-header');
    // }
  });

  // -----------------------------
  //  Scroll Reveal Animation
  // -----------------------------
  // Auto-add scroll-reveal class to major sections and elements that look good revealing
  $('.section, .feature-box, .service-item, .post, .project-item, .team-member, .cta-box').addClass('scroll-reveal');

  if ('IntersectionObserver' in window) {
    var observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.15
    };

    var observer = new IntersectionObserver(function (entries, Observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          $(entry.target).addClass('visible');
          Observer.unobserve(entry.target); // Only animate once
        }
      });
    }, observerOptions);

    $('.scroll-reveal').each(function () {
      observer.observe(this);
    });
  } else {
    // Fallback for older browsers
    $('.scroll-reveal').addClass('visible');
  }

  /* ========================================================================= */
  /*	Projects Pagination - 6 projects per page (2 rows x 3 columns)
  /* ========================================================================= */
  // Delay pagination initialization to run AFTER Filterizr (which has 500ms delay)
  setTimeout(function initProjectsPagination() {
    var $container = $('.filtr-container');
    var $pagination = $('.projects-pagination');

    if ($container.length === 0 || $pagination.length === 0) {
      return;
    }

    var $allProjects = $container.find('.filtr-item');
    var totalProjects = $allProjects.length;
    var projectsPerPage = 6; // 2 rows x 3 columns
    var totalPages = Math.ceil(totalProjects / projectsPerPage);
    var currentPage = 1;

    // Function to show projects for current page
    function showPage(page) {
      currentPage = page;
      var startIndex = (page - 1) * projectsPerPage;
      var endIndex = startIndex + projectsPerPage;

      $allProjects.each(function (index) {
        if (index >= startIndex && index < endIndex) {
          $(this).removeClass('pagination-hidden');
          $(this).css('display', ''); // Remove inline display to let CSS control
        } else {
          $(this).addClass('pagination-hidden');
        }
      });

      // Scroll to projects section
      if (page !== 1 || window.location.hash === '#projects-section') {
        $('html, body').animate({
          scrollTop: $('#projects-section').offset().top - 100
        }, 300);
      }

      updatePaginationUI();
    }

    // Function to update pagination UI
    function updatePaginationUI() {
      var $paginationList = $pagination.find('.pagination-list');
      $paginationList.empty();

      // Previous button
      if (currentPage > 1) {
        $paginationList.append('<li class="prev"><a href="#" data-page="' + (currentPage - 1) + '">&lt;</a></li>');
      }

      // Page numbers logic
      var startPage = 1;
      var endPage = totalPages;
      var showDots = false;

      if (totalPages <= 5) {
        // Show all pages if 5 or less
        startPage = 1;
        endPage = totalPages;
      } else {
        // Show first page, last page, current page, and neighbors
        if (currentPage <= 3) {
          startPage = 1;
          endPage = 4;
          showDots = true;
        } else if (currentPage >= totalPages - 2) {
          startPage = totalPages - 3;
          endPage = totalPages;
          showDots = true;
        } else {
          startPage = currentPage - 1;
          endPage = currentPage + 1;
          showDots = true;
        }
      }

      // First page
      if (startPage > 1) {
        $paginationList.append('<li' + (1 === currentPage ? ' class="active"' : '') + '><a href="#" data-page="1">1</a></li>');
        if (startPage > 2) {
          $paginationList.append('<li class="dots"><span>...</span></li>');
        }
      }

      // Middle pages
      for (var i = startPage; i <= endPage; i++) {
        var activeClass = (i === currentPage) ? ' class="active"' : '';
        $paginationList.append('<li' + activeClass + '><a href="#" data-page="' + i + '">' + i + '</a></li>');
      }

      // Last page
      if (endPage < totalPages) {
        if (endPage < totalPages - 1) {
          $paginationList.append('<li class="dots"><span>...</span></li>');
        }
        $paginationList.append('<li' + (totalPages === currentPage ? ' class="active"' : '') + '><a href="#" data-page="' + totalPages + '">' + totalPages + '</a></li>');
      }

      // Next button
      if (currentPage < totalPages) {
        $paginationList.append('<li class="next"><a href="#" data-page="' + (currentPage + 1) + '">&gt;</a></li>');
      }
    }

    // Event delegation for pagination clicks
    $pagination.on('click', '.pagination-list a', function (e) {
      e.preventDefault();
      var page = parseInt($(this).data('page'), 10);
      if (page && page !== currentPage) {
        showPage(page);
      }
    });

    // Initialize first page
    if (totalProjects > 0) {
      showPage(1);
    }
  }, 800); // 800ms delay to run after Filterizr (500ms)

})(jQuery);
