import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ErrorComponent } from './_utils/error/error.component';
import { AuthGuard } from './_helpers/auth.guard';
import { ProfilEtudiantComponent } from './profil/profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from './profil/profil-enseignant/profil-enseignant.component';
import { AdminModule } from './admin/admin.module';


const routes: Routes = [
  {
    path: '', loadChildren: () => import('./pulic/pulic.module')
    .then(m => m.PulicModule)
  },
  {path: 'admin', loadChildren: () => import('./admin/admin.module')
    .then(m => m.AdminModule), canActivate:[AuthGuard] 
  },

  {path: 'auth', loadChildren: () => import('./auth/auth.module')
  .then(m => m.AuthModule)
  },
  {
    path: 'profil', loadChildren: () => import('./profil/profil.module')
    .then(m => m.ProfilModule)
  },



  {path: '**', component: ErrorComponent}
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
