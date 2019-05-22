import {Injectable} from '@angular/core';
import {Router,CanActivate} from '@angular/router';
import {AuthenticaionService} from "./services/authenticaion.service";

@Injectable()
export class OnlyLoggedInUsersGuard implements CanActivate {

  constructor(private authenticationService: AuthenticaionService,public router: Router) {}

  canActivate() {
    if (this.authenticationService.userLoggedIn()) {
      return true;
    } else {
      window.alert('no permission');
      this.router.navigate(['login']);
      return false;
    }
  }
}
