import { Injectable } from '@angular/core';
import {BaseService} from './base.service'
import { HttpClient, HttpHeaders } from '@angular/common/http'
import {Observable} from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import {Campaign} from '../models/campaign';
import {CampaignList} from '../models/campaignlist';
import {CampaignDetails} from '../models/campaign-details';
import {Donate} from '../models/donate';
import {CampaignComment} from '../models/campaign-comment';
import {CommentList} from '../models/commentlist';
import 'rxjs/add/operator/map';

@Injectable()
export class CampaignService extends BaseService{

  private url = "campaigns/";
  constructor(private http:HttpClient) {
    super();
  }

  getCampaigns(limit,offset):Observable<CampaignList>{
    return this.http.get<CampaignList>(this.API_BASE_URL+this.url+"?limit="+limit+"&offset="+offset);
  }
  getCampaignsByCategoryId(categoryId,limit,offset):Observable<CampaignList>{
    return this.http.get<CampaignList>(this.API_BASE_URL+this.url+"?category_id="+categoryId+"&limit="+limit+"&offset="+offset);
  }
  getHighligthedCampaigns():Observable<Campaign[]>{
    return this.http.get<Campaign[]>(this.API_BASE_URL+this.url+"highlighted-campaigns/");
  }

  getCampaignDetails(slug):Observable<CampaignDetails>{
    return this.http.get<CampaignDetails>(this.API_BASE_URL+this.url+slug+"/");
  }

  getRecentDonation(id):Observable<Donate[]>{
    return this.http.get<Donate[]>(this.API_BASE_URL+this.url+"recent-donations/?campaign_id="+id);
  }

  getTopDonation(id):Observable<Donate[]>{
    return this.http.get<Donate[]>(this.API_BASE_URL+this.url+"top-donations/?campaign_id="+id);
  }
  getRelatedCampaigns(id):Observable<Campaign[]>{
    return this.http.get<Campaign[]>(this.API_BASE_URL+this.url+"related-campaigns/?campaign_id="+id);
  }

  getComments(id,limit,offset):Observable<CommentList>{
    return this.http.get<CommentList>(this.API_BASE_URL+this.url+id+"/comments/?limit="+limit+"&offset="+offset);
  }

  postComment(campaignId,comment):Observable<CampaignComment>{
    const httpOptions = {
        headers: new HttpHeaders({
          'Content-Type':  'application/x-www-form-urlencoded',
          'Authorization': 'Token '+localStorage.getItem("currentUser")
        })
    };
    //const data = new FormData();
    //data.append("campaign_id",campaignId);
    //data.append("comment",comment);
    return this.http.post<CampaignComment>(this.API_BASE_URL+this.url+campaignId+"/comments/",{campaign_id:campaignId,comment:comment},httpOptions);
  }

}
