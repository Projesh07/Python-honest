import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';

import { User } from '../models/user';
import { BaseService } from './base.service';
import {UserDetails} from "../models/user-details";
import {Donate} from "../models/donate";
import {UserDonationStat} from "../models/user-donation-stat";
import {UserProfile} from "../models/user-profile";

@Injectable()
export class UserService extends BaseService {

    constructor(private http: HttpClient) {
      super()
     }

    creat(user: User) {
        const httpOptions = {
            headers: new HttpHeaders({
              'Content-Type':  'application/json',
            })
        };


        return this.http.post(this.API_BASE_URL + 'rest-auth/registration/', user,httpOptions);
        // return this.http.post(this.API_BASE_URL + 'rest-auth/registration/', user);
    }
    update(firstName,lastName){
       const httpOptions = {
          headers: new HttpHeaders({
            'Content-Type':  'application/x-www-form-urlencoded',
            'Authorization': 'Token '+localStorage.getItem("currentUser")
          })
      };
      return this.http.post<UserDetails>(this.API_BASE_URL+"users/update/",{firstname:firstName,lastname:lastName},httpOptions);
    }
    imageUpload(file){
      const httpOptions = {
          headers: new HttpHeaders({
            //'Content-Type':  'multipart/form-data;boundary=BoUnDaRyStRiNg',
            //'Media_Type':  'multipart/form-data',
            //'Content-Disposition': 'attachment;filename='+file.name,
            'Authorization': 'Token '+localStorage.getItem("currentUser")
          })
      };
      const formData: FormData = new FormData();
      formData.append('file',file);
      return this.http.post<UserProfile>(this.API_BASE_URL+"users/upload-profile-image/",formData,httpOptions);
    }
    details(){
        const httpOptions = {
          headers: new HttpHeaders({
            'Content-Type':  'application/x-www-form-urlencoded',
            'Authorization': 'Token '+localStorage.getItem("currentUser")
          })
      };
      return this.http.get<UserDetails>(this.API_BASE_URL+"users/details/",httpOptions);

    }

    donations(){
        const httpOptions = {
          headers: new HttpHeaders({
            'Content-Type':  'application/x-www-form-urlencoded',
            'Authorization': 'Token '+localStorage.getItem("currentUser")
          })
      };
      return this.http.get<Donate[]>(this.API_BASE_URL+"users/donations/",httpOptions);

    }

    stat(){
      const httpOptions = {
          headers: new HttpHeaders({
            'Content-Type':  'application/x-www-form-urlencoded',
            'Authorization': 'Token '+localStorage.getItem("currentUser")
          })
      };
      return this.http.get<UserDonationStat>(this.API_BASE_URL+"users/donations/report/",httpOptions);
    }

    changeVisibility(is_private){
      const httpOptions = {
          headers: new HttpHeaders({
            'Content-Type':  'application/x-www-form-urlencoded',
            'Authorization': 'Token '+localStorage.getItem("currentUser")
          })
      };
      return this.http.post<boolean>(this.API_BASE_URL+"users/change-visibility/",{is_private:is_private},httpOptions);
    }



}
