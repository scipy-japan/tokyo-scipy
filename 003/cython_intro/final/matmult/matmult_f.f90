subroutine matmult_f(N, M, L, A, B, C)
    implicit none
    integer, intent(in) :: N, M, L
    real(8), intent(in) :: A(N, L), B(L, M)
    real(8), intent(out) :: C(N, M)

    integer :: i, j, k

    do i = 1, N
        do j = 1, M
            C(i, j) = 0.0d0
            do k = 1, L
                C(i, j) = C(i, j) + A(i, k) * B(k, j)
            enddo
        enddo
    enddo
end subroutine
