import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from './pages/home/home.component';
import {CampaignsComponent} from './pages/campaigns/campaigns.component'
import {CampaignDetailsComponent} from './pages/campaign-details/campaign-details.component'
import {LoginComponent} from './pages/login/login.component'
import {RegisterComponent} from './pages/register/register.component'
import {OnlyLoggedInUsersGuard} from "./guard";
const routes: Routes = [
   { path: '', component: HomeComponent},
   { path: 'campaigns', component: CampaignsComponent},
   { path: 'campaigns/:categoryId', component: CampaignsComponent},
   { path: 'login', component: LoginComponent},
   { path: 'register', component: RegisterComponent},
   { path: 'user-panel',loadChildren:'./modules/user/user.module#UserModule',canActivate: [OnlyLoggedInUsersGuard]},
   { path: ':slug', component: CampaignDetailsComponent},
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
