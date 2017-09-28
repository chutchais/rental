'use strict';

angular.module('rental').
    config(
        function(
          $locationProvider,
          $resourceProvider,
          $routeProvider
          ){


          $locationProvider.html5Mode({
              enabled:true
            })

          $resourceProvider.defaults.stripTrailingSlashes = false;
          $routeProvider.
              when("/", {
                // templateUrl: "/api/templates/about.html"
                // template: "<model-list></model-list>"
                // templateUrl: "/api/templates/about.html"
                // console.log('home')
              }).
              when("/rental", {
                // console.log('rental')
                template: "<rental-list></rental-list>"
              }).
              otherwise({
                  template: "Not Found"
              })

    });