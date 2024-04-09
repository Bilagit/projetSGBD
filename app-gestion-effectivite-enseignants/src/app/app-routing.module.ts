import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ErrorComponent } from './_utils/error/error.component';
import { AuthGuard } from './_helpers/auth.guard';

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

  {path: '**', component: ErrorComponent}
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
