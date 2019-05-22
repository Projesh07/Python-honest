import {Campaign} from "./campaign";
export interface CampaignList{
  count:number;
  next:string;
  previous:string;
  results:Campaign[];
}
