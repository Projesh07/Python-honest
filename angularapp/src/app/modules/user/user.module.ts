import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {UserRoutingModule} from "./user-routing.module";
import { LeftNavigationComponent } from './components/left-navigation/left-navigation.component';
import { UserDashboardStatComponent } from './components/user-dashboard-stat/user-dashboard-stat.component';
import { UserRecentDonationComponent } from './components/user-recent-donation/user-recent-donation.component';
import { UserDonationHistoryComponent } from './components/user-donation-history/user-donation-history.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { UserDashboardComponent } from './pages/user-dashboard/user-dashboard.component';
import {TopNavigationComponent} from "../../components/top-navigation/top-navigation.component";
import {AuthenticaionService} from "../../services/authenticaion.service";
import {AppRoutingModule} from "../../app-routing.module";
import { FormsModule }   from '@angular/forms';
@NgModule({
  imports: [
    CommonModule,
    UserRoutingModule,
    FormsModule
  ],
  declarations: [LeftNavigationComponent, UserDashboardStatComponent, UserRecentDonationComponent, UserDonationHistoryComponent, UserProfileComponent, UserDashboardComponent],
})
export class UserModule { }
