import { ReturnStatement } from '@angular/compiler/compiler';
import { Injectable } from '@angular/core';
import {Campaign} from './campaign-model';

import {User} from './campaign-model';
import {TopDonations,DonationComments,RegisterUser} from './campaign-model';
import { Headers, RequestOptions } from '@angular/http';



import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map'
import { environment } from '../environments/environment';


@Injectable()
export class CampaignService {

   constructor(private http: Http) {
   		 
    }




getCampaignByCategory(id):Observable<Campaign[]> {
        return this.http.get(environment.apiendpoint+'campaigns/?category_id='+id)
      	.map(response =>  <Campaign[]>response.json());
  }  


getCampaignDetails(slug):Observable<Campaign>{
         return this.http.get(environment.apiendpoint+'campaigns/'+slug+'/')
      	.map(response =>  <Campaign>response.json());
  }


getTopDonations():Observable<TopDonations[]>{

	      return this.http.get(environment.apiendpoint+'campaigns/top-donations/')
      	.map(response =>  <TopDonations[]>response.json());
}  

getRecentDonations():Observable<TopDonations[]>{

	      return this.http.get(environment.apiendpoint+'campaigns/recent-donations/')
      	.map(response =>  <TopDonations[]>response.json());
} 

getDonationComments(id):Observable<DonationComments[]>{

        return this.http.get(environment.apiendpoint+'campaigns/'+id+'/comments/')
        .map(response =>  <DonationComments[]>response.json());
}   



postRegister(user:RegisterUser):Observable<RegisterUser[]>{
  let headers = new Headers({ 'Content-Type': 'application/json' });
  let options = new RequestOptions({ headers: headers });

return this.http.post(environment.apiendpoint2+'rest-auth/registration/',user, options)
.map(response =>  <RegisterUser[]>response.json());
              
} 

getUser(id):Observable<User[]>{

        return this.http.get(environment.apiendpoint+'users/'+id)
        .map(response =>  <User[]>response.json());
}   



}
