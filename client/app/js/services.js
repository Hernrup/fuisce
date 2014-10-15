'use strict';

/* Services */

var fuisceServices = angular.module('fuisceServices', ['ngResource', 'angular-growl']);

fuisceServices.config(['growlProvider', function(growlProvider) {
  growlProvider.globalTimeToLive(6000);
  growlProvider.globalDisableCloseButton(true);
  growlProvider.globalPosition('bottom-center');
  growlProvider.globalDisableCountDown(true);
}]);

fuisceServices.factory('ApiService', ['$resource', '$http', '$exceptionHandler', 'growl', 
	function($resource, $http, exception, growl){
  


  function Review(user_id, event_id, whisky_id) {
  	var self = this;

  	self.user = user_id;
  	self.event = event_id;
  	self.whisky = whisky_id;
  	self.points = 1;
  	self.nose = "";
  	self.taste = "";
  	self.finish = "";
  	self.comment = "";
  	self.smokyness = 1;
  	self.strength = 1;
  }


  function reviewFactory(user_id, event_id, whisky_id){
  	return new Review(user_id, event_id, whisky_id);
  }

  function getEvents(callback){
  	
  	$http.get('/api/event/',{})
    .success(function(data) {
    	callback(data);
    })
    .error(function(data, status, headers, config) {
     	growl.error('Failed to load events');
    })
  }

  function getUsers(event_id, callback){
  	$http.get('/api/user/', {params: {event: event_id, rnd: (new Date).getTime()}})
    .success(function(data) {
    	callback(data);
    })
    .error(function(data, status, headers, config) {
     	growl.error('Failed to load users', data, status);
    })
  }

  function getWhiskys(event_id, callback){
  	
  	$http.get('/api/whisky/' , {params: {event: event_id, rnd: (new Date).getTime()}})
    .success(function(data) {
    	callback(data);
    })
    .error(function(data, status, headers, config) {
     	growl.error('Failed to load events',data,status);
    })
  }

  function saveReview(review, callback){
  	$http.post('/api/review/' , {params: {review: review, rnd: (new Date).getTime()}})
    .success(function(data) {
    	callback(data);
    })
    .error(function(data, status, headers, config) {
     	growl.error('Failed to post review',data,status);
    })
  }

  return {
    getUsers: getUsers,
    getEvents: getEvents,
    getWhiskys: getWhiskys,
    reviewFactory: reviewFactory,
    saveReview: saveReview
  };

}]);

