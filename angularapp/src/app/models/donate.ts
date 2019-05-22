import {Campaign} from "./campaign";
import {UserDetails} from "./user-details";
export interface Donate{
  id:number;
  amount:number;
  donate_at:string;
  campaign:Campaign;
  user:UserDetails;
}
