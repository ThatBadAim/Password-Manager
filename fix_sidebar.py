with open('CipherVault/MainWindow.xaml', 'r') as f:
    content = f.read()

search1 = '''                            <Border x:Name="ActiveIndicator" Width="4" HorizontalAlignment="Left" Background="Transparent" CornerRadius="0,4,4,0"/>
                            <ContentPresenter Margin="24,12"/>
                        </Grid>'''
replace1 = '''                            <Border x:Name="ActiveIndicator" Width="4" HorizontalAlignment="Left" Background="Transparent" CornerRadius="0,4,4,0"/>
                            <StackPanel Orientation="Horizontal" Margin="24,12">
                                <TextBlock FontFamily="Segoe MDL2 Assets" FontSize="14" Margin="0,0,12,0" VerticalAlignment="Center" Text="{Binding RelativeSource={RelativeSource AncestorType=RadioButton}, Path=Tag}"/>
                                <ContentPresenter VerticalAlignment="Center"/>
                            </StackPanel>
                        </Grid>'''
content = content.replace(search1, replace1)

search2 = '''                <!-- Navigation -->
                <StackPanel Grid.Row="1">
                    <RadioButton Content="Vault" IsChecked="True" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Favorites" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Security Audit" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Settings" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                </StackPanel>'''
replace2 = '''                <!-- Navigation -->
                <StackPanel Grid.Row="1">
                    <RadioButton Content="Vault" Tag="&#xE8F1;" IsChecked="True" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Favorites" Tag="&#xE734;" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Security Audit" Tag="&#xE81C;" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                    <RadioButton Content="Settings" Tag="&#xE713;" Style="{StaticResource SidebarMenuBtn}" GroupName="Nav"/>
                </StackPanel>'''
content = content.replace(search2, replace2)

with open('CipherVault/MainWindow.xaml', 'w') as f:
    f.write(content)
