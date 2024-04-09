import { CanActivateFn } from '@angular/router';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot,RouterStateSnapshot,UrlTree,Router } from '@angular/router';
import { Observable } from 'rxjs';

/*export const authGuard: CanActivateFn = (route, state) => {
  return false;
};*/
@Injectable({
  providedIn: 'root'
})
export class AuthGuard {

  constructor(private router: Router) {}
  canActivate: CanActivateFn = (
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree => {
    // Votre logique de vérification d'authentification ici
    return this.router.navigate(['auth']); // ou false en fonction de la logique d'authentification
  };
}
/*export class AuthGuard implements CanActivateFn {

  constructor(private router: Router) {}

  canActivate(
    route:ActivatedRouteSnapshot,
    state:RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      return true;
    }
}*/