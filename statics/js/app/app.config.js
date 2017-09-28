'use strict';

angular.module('try').
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
                templateUrl: "/templates/angular/app/about.html"
              }).
              when("/distribute", {
                template: "<model-list></model-list>"
              }).
              when("/distribute/:model", {
                template: "<model-list></model-list>"
              }).
              when("/distribute/:model/:station", {
                template: "<model-list></model-list>"
              }).
              when("/distribute/:model/:station/:parameter", {
                template: "<parameter-detail></parameter-detail>"
              }).
              when("/spc", {
                templateUrl: "/api/templates/about.html"
              }).
              when("/spc/:model", {
                template: "<spc-station-list></spc-station-list>"
              }).
              when("/spc/:model/:station", {
                template: "<spc-station-list></spc-station-list>"
              }).
              when("/spc/:model/:station/ALL", {
                template: "<spc-tester-detail></spc-tester-detail>"
              }).
              when("/spc/:model/:station/ALL/:parameter", {
                template: "<spc-parameter-detail></spc-parameter-detail>"
              }).
              when("/spc/:model/:station/:tester", {
                template: "<spc-station-detail></spc-station-detail>"
              }).
              when("/about", {
                template: "<blog-list></blog-list>"
              }).
              when("/blog", {
                  template: "<blog-list></blog-list>",
                  // redirectTo: '/'
              }).
              when("/blog/:slug", {
                  template: "<blog-detail></blog-detail>"
              }).
              when("/login", {
                  template: "<login-detail></login-detail>",
                  // redirectTo: '/'
              }).
              when("/logout", {
                  // template: "<login-detail></login-detail>",
                  redirectTo: '/login'
              }).
               when("/register", {
                  template: "<register-detail></register-detail>",
                  // redirectTo: '/'
              }).
              otherwise({
                  template: "Not Found"
              })

    });