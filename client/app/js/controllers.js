'use strict';

/* Controllers */

var fuisceControllers = angular.module('fuisceControllers', ['angular-growl']);

fuisceControllers.config(['growlProvider', function(growlProvider) {
  growlProvider.globalTimeToLive(6000);
  growlProvider.globalDisableCloseButton(true);
  growlProvider.globalPosition('bottom-center');
  growlProvider.globalDisableCountDown(true);
}]);

fuisceControllers.controller('ReviewController', ['$scope', '$http', 'ApiService', 'growl',
  function($scope, $http, ApiService, growl) {

    reloadEvents($scope);
    reloadReview($scope);

    $scope.selectedUser = {id: 0};
    $scope.selectedEvent = {id: 0};
    $scope.selectedWhisky = {id: 0};
 
    $scope.rangeHundred = (Array.apply(null, Array(100)).map(function (_, i) {return (i+1);})).reverse();
    $scope.rangeFive = (Array.apply(null, Array(5)).map(function (_, i) {return i+1;}));
    $scope.enableReviewPost = false;

    $scope.eventChanged = function (item) {
      reloadUsers($scope);
      growl.info('Thats a fine place to be!')
    }


    $scope.userChanged = function (item) {
      reloadWhiskys($scope);
      reloadReview($scope);
      growl.info('Not you again...')
    }

    $scope.whiskyChanged = function (item) {
      reloadReview($scope);
      growl.info('Alright, have at it!')
    }

    function reloadEvents($scope){
      ApiService.getEvents(function(data){
        $scope.events = data.events;
        // $scope.selectedEvent = data.events[0]
        // $scope.eventChanged($scope.selectedEvent)
      })
    }

    function reloadUsers($scope){
      ApiService.getUsers($scope.selectedEvent.id, function(data){
        $scope.users = data.users;
        // $scope.selectedUser = data.users[0];
        // $scope.userChanged($scope.selectedUser)
      })
    }

    function reloadWhiskys($scope){
      ApiService.getWhiskys($scope.selectedEvent.id, function(data){
        $scope.whiskys = data.whiskys;
        // $scope.selectedWhisky = data.whiskys[0];
        // $scope.whiskyChanged($scope.selectedWhisky);
      })
    }

    function reloadReview($scope){
      $scope.review = ApiService.reviewFactory($scope.selectedUser, $scope.selectedEvent, $scope.selectedWhisky);
    }

    $scope.submitReview = function(){
      $scope.enableReviewPost = true;
      ApiService.saveReview($scope.review, function(){
        $scope.selectedWhisky = {id: 0}; 
        reloadReview($scope);
        $scope.enableReviewPost = false;
        growl.success("Thats what you think!? I better save that one for later!")
      })
    }


    


}]);
